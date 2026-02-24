import sys
import os

sys.path.append(os.path.abspath("src"))

from src.extractor import extract_text_from_pdf
from src.cleaner import clean_text
from src.similarity import compute_similarity
from src.skills import skill_match_score
from src.skills import generate_suggestions

pdf_path = r"C:\Users\punee\Desktop\Resumes\Dhanusha_katakamEdiga Resume.pdf"

resume_text = extract_text_from_pdf(pdf_path)

if not resume_text:
    print("ERROR : NO TEXT EXTRACTED")
    exit()
    
resume_clean = clean_text(resume_text)
resume_clean=resume_clean[:800]




job_description = """
We are hiring a Machine Learning Engineer.
Required skills: Python, Machine Learning, NLP, TensorFlow, Deep Learning, Data Analysis.
Experience with scikit-learn and model deployment is a plus.
"""

job_clean = clean_text(job_description)
semantic_score = compute_similarity(resume_clean,job_clean)

if semantic_score > 0.95:
    semantic_score = 0.95
    
semantic_percent = semantic_score * 100

skill_score, matched_skills,missing_skills = skill_match_score(resume_clean, job_clean)
final_score = (semantic_percent * 0.6) + (skill_score * 0.4)

suggestions = generate_suggestions(missing_skills, matched_skills)

print("\n===== RESULTS =====")

print("Semantic score:", round(semantic_percent,2), "%")
print("Skill score:", round(skill_score,2), "%")
print("Matched score:", matched_skills)

print("\n FINAL ATS SCORE:", round(final_score, 2), "%")
print("\n SUGGESTIONS:")
for s in suggestions:
    print("-", s)