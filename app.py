import streamlit as st
import os
import fitz  # PyMuPDF
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Automatically download spaCy model on Streamlit Cloud
os.system("python -m spacy download en_core_web_sm")

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Default Job Description
DEFAULT_JD = """
We are looking for a candidate with strong skills in Python, Machine Learning, Natural Language Processing (NLP),
TensorFlow or PyTorch, and REST API development. Understanding of data preprocessing and model deployment is a plus.
"""

# Clean text from special chars (very important for spaCy)
def safe_clean(text):
    try:
        text = text.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
        return ''.join([c if ord(c) < 128 else '' for c in text])
    except:
        return ""

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return safe_clean(text)
    except Exception as e:
        return None

# NLP keyword extraction
def extract_keywords(text):
    doc = nlp(text.lower())
    return ' '.join([token.text for token in doc if token.is_alpha and not token.is_stop])

def get_top_keywords(text, top_n=10):
    doc = nlp(text.lower())
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    freq = {}
    for word in keywords:
        freq[word] = freq.get(word, 0) + 1
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [kw[0] for kw in sorted_keywords[:top_n]]

def compute_match_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)

# Streamlit UI
st.set_page_config(page_title="Resume Screener", layout="centered")
st.title("Ì≥Ñ AI Resume Screener using NLP")
st.write("Upload your resume and job description to compute skill match and see keyword insights.")

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type="pdf")
job_description = st.text_area("Paste the Job Description", value=DEFAULT_JD, height=200)

if uploaded_file and job_description:
    with st.spinner("Extracting and analyzing..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        if not resume_text:
            st.error("‚ùå Could not read or clean the uploaded PDF.")
            st.stop()

        resume_clean = extract_keywords(resume_text)
        jd_clean = extract_keywords(job_description)

        score = compute_match_score(resume_clean, jd_clean)

        st.success(f"‚úÖ Resume Match Score: {score}%")

        # Explanation
        if score >= 75:
            explanation = "Excellent match. Your resume strongly aligns with the job description."
        elif score >= 50:
            explanation = "Moderate match. Your resume covers many areas but could be improved."
        else:
            explanation = "Low match. Your resume has few overlaps with the job description."

        st.markdown("### Ì≥å Explanation")
        st.info(explanation)

        st.markdown("### Ì¥ç Top Keywords in Resume")
        st.write(", ".join(get_top_keywords(resume_text)))

        st.markdown("### Ì≥ã Keywords in Job Description")
        st.write(", ".join(get_top_keywords(job_description)))

