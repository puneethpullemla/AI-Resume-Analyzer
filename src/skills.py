def skill_match_score(resume_text,job_description):
    resume_text = resume_text.lower()
    job_description= job_description.lower()
    
    skills = [
    "python", "machine learning", "ml",
    "nlp", "natural language processing",
    "tensorflow", "deep learning",
    "data analysis", "sql", "pandas",
    "scikit-learn", "deployment", "model deployment"
]
    
    resume_skills = [skill for skill in skills if skill in resume_text]
    job_skills = [skill for skill in skills if skill in job_description]

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_skills)) * 100

    return score, matched_skills, missing_skills , resume_skills

def generate_suggestions(missing_skills, resume_skills):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Add projects or experience related to '{skill}'")

    if len(missing_skills) == 0:
        suggestions.append("Great match! Your resume aligns well with the job description")

   
    if len(missing_skills) > 0:
        if "machine learning" not in resume_skills:
            suggestions.append("Include Machine Learning projects")

        if "model deployment" not in resume_skills:
            suggestions.append("Show deployment experience using Streamlit or Flask")

    return list(set(suggestions))