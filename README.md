# Ì∑† Resume Screener using NLP & Streamlit

An AI-powered web application that analyzes resume PDFs and matches them to job descriptions using Natural Language Processing (NLP). It extracts relevant keywords, computes a match score using TF-IDF and cosine similarity, and displays results interactively via a Streamlit web interface.

---

## Ì∫Ä Features

- Ì≥Ñ Upload a PDF resume and compare it against any job description
- Ì∑† Uses spaCy NLP pipeline for keyword extraction
- Ì≥ä Computes match score using TF-IDF & cosine similarity
- Ì¥ç Highlights top keywords from both resume and job description
- Ì∂•Ô∏è Interactive, browser-based UI with Streamlit

---

## Ì≥Å Project Structure

resume-screener/
‚îú‚îÄ‚îÄ app.py # Streamlit web app
‚îú‚îÄ‚îÄ main.py # CLI version (terminal-based)
‚îú‚îÄ‚îÄ requirements.txt # All Python dependencies
‚îú‚îÄ‚îÄ .gitignore # Ignore venv, pycache, and resume.pdf
‚îî‚îÄ‚îÄ README.md # This file

---

## Ì∑∞ Tech Stack

- Python
- spaCy (`en_core_web_sm`)
- pdfminer.six
- scikit-learn (TF-IDF & cosine similarity)
- Streamlit (for web UI)

---

## Ì∑™ How It Works

1. User uploads a resume (PDF)
2. Text is extracted from the file
3. Stopwords and irrelevant tokens are removed using spaCy
4. TF-IDF vectors are computed between the resume and job description
5. Cosine similarity is calculated and displayed as a **match percentage**
6. Top 10 keywords from both texts are displayed for quick insight

---

## Ì∂•Ô∏è Run the Streamlit App Locally

### 1. Clone the repo

```bash
git clone https://github.com/Rajeswararao89/resume-screener-nlp.git
cd resume-screener-nlp
Ì≥Ñ Sample Output (Terminal)
=========== Resume Screening Result ===========

Match Score: 78.5%

Top Keywords in Resume:
python, docker, devops, aws, cicd, jenkins, terraform, cloud, pipeline, automation

Key Job Description Keywords:
python, machine, learning, nlp, tensorflow, deployment, model, skills, data, api

Explanation: Excellent match. Resume strongly aligns with job requirements.

===============================================
Ì±§ Author
Rajeswara Rao Jangiti
Ì≥ç DevOps | NLP | AI Engineering
GitHub ‚Ä¢ LinkedIn
