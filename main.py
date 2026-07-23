# TO RUN: In terminal, make sure youre on correct path: uv run python -m streamlit run main.py (OR if not using uv: python -m streamlit run main.py)
# Anything page state changes, entire python file is re-rain again. But the state is saved. E.g. file uploaded -> entire script re-runs, but file is still stored in variable. Same with job_role
# THIS IS NOT AN AI AGENT. We directly invoke LLM here


import streamlit as st
import PyPDF2
from docx import Document
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

def setup_page():
    # Streamlit page configuration must happen before
    # any UI elements are displayed.
    st.set_page_config(
        page_title="AI Resume Critiquer",
        page_icon="📃",
        layout="centered"
    )


def create_ui():
    # Creates the visible components of the application
    st.title("AI Resume Critiquer")
    st.markdown(
        "Upload your resume and get AI-powered feedback tailored to your needs!"
    )

    uploaded_file = st.file_uploader(
        "Upload your resume (PDF, DOCX or TXT)",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=False
    )

    job_role = st.text_input(
        "Enter the job role you're targeting (optional)"
    )

    return uploaded_file, job_role


# Extract text from different supported file types.
# Currently supports PDF and plain text files.
def extract_text_from_file(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file)

    # TXT files are read as bytes, then decoded into a normal string.
    return file.read().decode("utf-8")


def extract_text_from_pdf(pdf_file):
    # PyPDF2 reads PDF content page by page.
    # Note: Image-based/scanned PDFs may not return any text because
    # they require OCR instead of normal text extraction.
    reader = PyPDF2.PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        # Some pages may return None if no extractable text exists.
        text += (page.extract_text() or "") + "\n"

    return text

def extract_text_from_docx(docx_file):
    document = Document(docx_file)

    text = []

    for paragraph in document.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


def create_resume_prompt(resume_text, job_role):
    # If the user does not specify a role, provide general resume feedback.
    target = job_role if job_role else "general job applications"

    return f"""
Please analyze this resume and provide constructive feedback.

Focus on:
1. Content clarity and impact
2. Skills presentation
3. Experience descriptions
4. Specific improvements for {target}

Resume:
{resume_text}

Provide:
- 3 strengths
- 3 weaknesses
- 5 specific improvements

Keep your response under 800 words.
"""


@st.cache_resource
def get_llm():
    # Streamlit reruns the entire Python script whenever a widget changes.
    # cache_resource prevents recreating the LLM client every rerun.
    return ChatOllama(
        model="qwen3:4b",
        temperature=0.7
    )


def analyze_resume(resume_text, job_role):
    llm = get_llm()

    # This application directly sends prompts to an LLM.
    # It is not an AI agent with tools, memory, or autonomous planning.
    response = llm.invoke([
        SystemMessage(
            content=(
                "You are an expert resume reviewer with years of "
                "experience in HR and recruitment."
            )
        ),
        HumanMessage(
            content=create_resume_prompt(resume_text, job_role)
        )
    ])

    return response.content


def handle_resume_analysis(uploaded_file, job_role):

    # Validate that a file was provided before processing.
    if not uploaded_file:
        st.error("Please upload a file first")
        return

    try:
        resume_text = extract_text_from_file(uploaded_file)

        if not resume_text.strip():
            # Prevent sending empty content to the LLM.
            st.error("File does not contain readable text")
            return

        st.write("Resume characters:", len(resume_text))
        st.write(
            "Approx tokens:",
            int(len(resume_text.split()) * 1.3)
        )

        # LLM inference can take time, so show a loading indicator.
        with st.spinner("Analyzing resume..."):
            result = analyze_resume(
                resume_text,
                job_role
            )

        st.markdown("### Analysis Results")
        st.markdown(result)

    except Exception as e:
        # Display errors gracefully instead of crashing the app.
        st.error(f"An error occurred: {e}")



def main():

    setup_page()

    uploaded_file, job_role = create_ui()

    # st.button() only returns True during the run where the user clicks it.
    # This prevents expensive LLM calls from happening on every Streamlit rerun.
    if st.button("Analyze Resume"):
        handle_resume_analysis(
            uploaded_file,
            job_role
        )

if __name__ == "__main__":
    main()