# AI Resume Critiquer

A small side project I built while job hunting and learning more about LLM-powered applications. 🙂

AI Resume Critiquer is a resume analysis application built with **Python**, **Streamlit**, **LangChain**, and **Hugging Face Inference Providers**. It accepts PDF, DOCX or TXT resumes and provides actionable feedback tailored to a target job role.

Inference runs on **`openai/gpt-oss-20b`**, a 20B-parameter open-weight model served through Hugging Face's Inference Providers router. The app originally ran on a locally hosted model via Ollama; it was migrated to Hugging Face so it could be deployed publicly without requiring users to run their own model.

For reference: a 636 word resume (826 tokens) takes roughly **5 seconds** to analyse.

Test it out: https://smart-resume-critique.streamlit.app/

---

## Features

* Upload resumes in **PDF**, **DOCX** or **TXT** format
* Extract text from PDFs using **PyPDF2** and from Word documents using **python-docx**
* AI-powered resume analysis returning 3 strengths, 3 weaknesses and 5 specific improvements
* Tailor feedback to a specific job role
* **2,000 word input cap** so token cost stays predictable regardless of resume length
* **Result caching** — re-analysing the same resume and role returns instantly without a second API call

---

## Tech Stack

* Python
* Streamlit
* LangChain (`langchain-huggingface`)
* Hugging Face Inference Providers — `openai/gpt-oss-20b`
* PyPDF2 / python-docx

---

## Prerequisites

Before running the application, make sure you have:

* Python 3.11+
* uv
* A free [Hugging Face account](https://huggingface.co/join) and an access token

Install **uv**:

```bash
pip install uv
```

### Getting a Hugging Face token

1. Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Create a token with **Read** permission
3. Save it — you'll add it to your `.env` file below

Free accounts receive a small monthly Inference Providers credit, which is enough for casual use. Usage can be monitored at [huggingface.co/settings/billing](https://huggingface.co/settings/billing).

---

## Installation

### Clone the repository

```bash
git clone https://github.com/bchoongwj/AI-Resume-Critiquer.git
cd AI-Resume-Critiquer
```

### Install dependencies

```bash
uv sync
```

### Add your API token

Copy `.env.example` to `.env` and fill in your token:

```bash
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
```

### Run the application

```bash
uv run python -m streamlit run main.py
(OR if not using uv: python -m streamlit run main.py)
```

The application will open automatically in your browser.

---

## Deployment

The app is deployable to **Streamlit Community Cloud** straight from this repository:

1. Connect the repo at [share.streamlit.io](https://share.streamlit.io), with `main.py` as the entry point
2. Under **Advanced settings → Secrets**, add:

   ```toml
   HUGGINGFACEHUB_API_TOKEN = "hf_your_token_here"
   ```

The app reads its token from Streamlit secrets when deployed and from `.env` when run locally, so the same code works in both environments.

---

## Screenshots

### Upload Resume

<p align="center">
  <img src="assets/Resume%20Critique%20Results%201.png" width="850">
</p>

### AI Resume Analysis

<p align="center">
  <img src="assets/Resume%20Critique%20Results%202.png" width="850">
</p>

### Detailed Feedback

<p align="center">
  <img src="assets/Resume%20Critique%20Results%203.png" width="850">
</p>

---

## Future Improvements

* ATS compatibility scoring
* Resume-to-job description matching
* Streaming AI responses
* Support for multiple LLM models
* Export analysis to PDF

---

## License
MIT
This project is intended for learning and portfolio purposes.
