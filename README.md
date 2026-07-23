# AI Resume Critiquer

A small side project I built while job hunting and learning more about local LLM applications. 🙂

AI Resume Critiquer is a resume analysis application built with **Python**, **Streamlit**, **LangChain**, and **Ollama**. It accepts PDF or TXT resumes and provides actionable feedback tailored to a target job role using a **locally hosted Large Language Model (LLM)**. Since inference runs locally through Ollama, no external AI APIs or API keys are required.

For reference: For a 6944 word resume, it took approximately 1236 tokens, and slightly under 2 minutes to process

---

## Features

* Upload resumes in **PDF** or **TXT** format
* Extract text from PDF documents using **PyPDF2**
* AI-powered resume analysis using a local LLM
* Tailor feedback to a specific job role
* Runs entirely on your own machine with **Ollama**

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* PyPDF2

---

## Prerequisites

Before running the application, make sure you have installed:

* Python 3.13+
* Ollama
* uv

Install **uv**:

```bash
pip install uv
```

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

### Download the LLM

```bash
ollama pull qwen3:4b
```

### Start Ollama

If Ollama isn't already running:

```bash
ollama serve
```

### Run the application

```bash
uv run streamlit run main.py
```

The application will open automatically in your browser.

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
* Support for DOCX resumes
* Streaming AI responses
* Support for multiple LLM models
* Export analysis to PDF

---

## License

This project is intended for learning and portfolio purposes.
