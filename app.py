import streamlit as st
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Job Description (editable)
DEFAULT_JD = """
We are looking for a candidate with strong skills in Python, Machine Learning, Natural Language Processing (NLP),
TensorFlow or PyTorch, and REST API development. Understanding of data preprocessing and model deployment is a plus.
"""

# Extract clean keywords
def extract_keywords(text):
    doc = nlp(text.lower())
    return ' '.join([token.text for token in doc if token.is_alpha and not token.is_stop])

# Get top N keywords
def get_top_keywords(text, top_n=10):
    doc = nlp(text.lower())
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    freq = {}
    for word in keywords:
        freq[word] = freq.get(word, 0) + 1
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [kw[0] for kw in sorted_keywords[:top_n]]

# Match score
def compute_match_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)

# PDF text extractor
def extract_text_from_pdf(uploaded_file):
    return extract_text(uploaded_file)

# UI
st.title("Ì∑† AI Resume Screener")
st.write("Upload your resume and match it against a job description using NLP.")

uploaded_file = st.file_uploader("Ì≥Ñ Upload your resume PDF", type="pdf")
job_description = st.text_area("Ì≥ù Paste the Job Description here", value=DEFAULT_JD, height=200)

if uploaded_file and job_description:
    with st.spinner("Processing..."):
        raw_resume = extract_text_from_pdf(uploaded_file)
        clean_resume = extract_keywords(raw_resume)
        clean_jd = extract_keywords(job_description)

        score = compute_match_score(clean_resume, clean_jd)
        resume_keywords = get_top_keywords(raw_resume)
        jd_keywords = get_top_keywords(job_description)

    st.success(f"‚úÖ Resume Match Score: {score}%")

    if score >= 75:
        explanation = "Excellent match. Resume strongly aligns with the job requirements."
    elif score >= 50:
        explanation = "Moderate match. Resume covers many important areas but can be improved."
    else:
        explanation = "Low match. Resume has few overlaps with the job description."

    st.markdown("### Ì≥å Explanation")
    st.info(explanation)

    st.markdown("### Ì¥ç Top Keywords in Resume")
    st.write(", ".join(resume_keywords))

    st.markdown("### Ì∑æ Key Job Description Keywords")
    st.write(", ".join(jd_keywords))

