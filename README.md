# ν·  Resume Screener using NLP & Streamlit

An AI-powered web application that analyzes resume PDFs and matches them to job descriptions using Natural Language Processing (NLP). It extracts relevant keywords, computes a match score using TF-IDF and cosine similarity, and displays results interactively via a Streamlit web interface.

---

## νΊ Features

- ν³ Upload a PDF resume and compare it against any job description
- ν·  Uses spaCy NLP pipeline for keyword extraction
- ν³ Computes match score using TF-IDF & cosine similarity
- ν΄ Highlights top keywords from both resume and job description
- νΆ₯οΈ Interactive, browser-based UI with Streamlit

---

## ν³ Project Structure

resume-screener/
βββ app.py # Streamlit web app
βββ main.py # CLI version (terminal-based)
βββ requirements.txt # All Python dependencies
βββ .gitignore # Ignore venv, pycache, and resume.pdf
βββ README.md # This file

---

## ν·° Tech Stack

- Python
- spaCy (`en_core_web_sm`)
- pdfminer.six
- scikit-learn (TF-IDF & cosine similarity)
- Streamlit (for web UI)

---

## ν·ͺ How It Works

1. User uploads a resume (PDF)
2. Text is extracted from the file
3. Stopwords and irrelevant tokens are removed using spaCy
4. TF-IDF vectors are computed between the resume and job description
5. Cosine similarity is calculated and displayed as a **match percentage**
6. Top 10 keywords from both texts are displayed for quick insight

---

## νΆ₯οΈ Run the Streamlit App Locally

### 1. Clone the repo

```bash
git clone https://github.com/Rajeswararao89/resume-screener-nlp.git
cd resume-screener-nlp
ν³ Sample Output (Terminal)
=========== Resume Screening Result ===========

Match Score: 78.5%

Top Keywords in Resume:
python, docker, devops, aws, cicd, jenkins, terraform, cloud, pipeline, automation

Key Job Description Keywords:
python, machine, learning, nlp, tensorflow, deployment, model, skills, data, api

Explanation: Excellent match. Resume strongly aligns with job requirements.

===============================================
ν±€ Author
Rajeswara Rao Jangiti
ν³ DevOps | NLP | AI Engineering
GitHub β’ LinkedIn
