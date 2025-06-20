import streamlit as st
import fitz  # PyMuPDF
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model (already installed via requirements.txt)
nlp = spacy.load("en_core_web_sm")

# -------------------- Utility Functions --------------------

# Clean corrupted characters before NLP
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
                page_text = page.get_text()
                text += page_text
            return safe_clean(text)
    except Exception as e:
        return None

# Extract keywords for scoring
def extract_keywords(text):
    try:
        doc = nlp(text.lower())
        return ' '.join([token.text for token in doc if token.is_alpha and not token.is_stop])
    except:
        return ""

def get_top_keywords(text, top_n=10):
    try:
        doc = nlp(text.lower())
        keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
        freq = {}
        for word in keywords:
            freq[word] = freq.get(word, 0) + 1
        sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [kw[0] for kw in sorted_keywords[:top_n]]
    except:
        return []

def compute_match_score(resume_text, jd_text):
    try:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        score = cosine_similarity(vectors[0:1], vectors[1:2])
        return round(score[0][0] * 100, 2)
    except:
        return 0

# -------------------- Streamlit UI --------------------

st.set_page_config(page_title="Resume Screener", layout="centered")
st.title("Ì≥Ñ Resume Screener using NLP")

st.markdown("Upload your resume (PDF) and paste a job description to get match score and keyword insights.")

uploaded_file = st.file_uploader("Ì≥Å Upload Resume (PDF)", type="pdf")

default_jd = """
We are looking for a candidate with strong skills in Python, Machine Learning, Natural Language Processing (NLP),
TensorFlow or PyTorch, and REST API development. Understanding of data preprocessing and model deployment is a plus.
"""
job_description = st.text_area("Ì≥ù Paste Job Description", value=default_jd, height=200)

if uploaded_file and job_description:
    with st.spinner("Processing..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        if not resume_text:
            st.error("‚ùå Could not extract text from PDF. Please try a different file.")
            st.stop()

        resume_clean = extract_keywords(resume_text)
        jd_clean = extract_keywords(job_description)

        score = compute_match_score(resume_clean, jd_clean)

        st.success(f"‚úÖ Resume Match Score: {score}%")

        if score >= 75:
            explanation = "Excellent match. Your resume strongly aligns with the job description."
        elif score >= 50:
            explanation = "Moderate match. Your resume covers many relevant areas."
        else:
            explanation = "Low match. Consider tailoring your resume to better fit the job description."

        st.markdown("### Ì≥å Explanation")
        st.info(explanation)

        st.markdown("### Ì¥ç Top Keywords in Resume")
        st.write(", ".join(get_top_keywords(resume_text)))

        st.markdown("### Ì≥ã Top Keywords in Job Description")
        st.write(", ".join(get_top_keywords(job_description)))

