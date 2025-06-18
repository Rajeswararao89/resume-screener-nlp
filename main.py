import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Path to your resume
resume_path = "resume.pdf"

# Sample job description
job_description = """
We are looking for a candidate with strong skills in Python, Machine Learning, Natural Language Processing (NLP),
TensorFlow or PyTorch, and REST API development. Understanding of data preprocessing and model deployment is a plus.
"""

# Extract text from PDF
def extract_resume_text(path):
    return extract_text(path)

# Extract meaningful keywords
def extract_keywords(text):
    doc = nlp(text.lower())
    return ' '.join([token.text for token in doc if token.is_alpha and not token.is_stop])

# Get top N keywords as a list
def get_top_keywords(text, top_n=10):
    doc = nlp(text.lower())
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    freq = {}
    for word in keywords:
        freq[word] = freq.get(word, 0) + 1
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [kw[0] for kw in sorted_keywords[:top_n]]

# Compute cosine similarity score
def match_resume_with_job(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)

# Main workflow
resume_raw = extract_resume_text(resume_path)
clean_resume = extract_keywords(resume_raw)
clean_jd = extract_keywords(job_description)

# Match score
score = match_resume_with_job(clean_resume, clean_jd)

# Output
print("\n=========== Resume Screening Result ===========\n")
print(f"Match Score: {score}%\n")

print("Top Keywords in Resume:")
print(", ".join(get_top_keywords(resume_raw)))

print("\nKey Job Description Keywords:")
print(", ".join(get_top_keywords(job_description)))

# Explanation
if score >= 75:
    explanation = "Excellent match. Resume strongly aligns with the job requirements."
elif score >= 50:
    explanation = "Moderate match. Resume covers many important areas but can be improved."
else:
    explanation = "Low match. Resume has few overlaps with the job description."

print(f"\nExplanation: {explanation}")
print("\n===============================================\n")

