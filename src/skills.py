def skill_match_score(resume_text,job_description):
    resume_text = resume_text.lower()
    job_description= job_description.lower()
    
    skills = [
    # 🔹 Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "go", "rust", "kotlin", "swift", "r", "matlab", "bash", "shell scripting",

    # 🔹 Web Development - Frontend
    "html", "css", "sass", "bootstrap", "tailwind", "javascript",
    "react", "angular", "vue", "next.js", "nuxt.js",

    # 🔹 Web Development - Backend
    "node.js", "express.js", "django", "flask", "spring boot",
    "fastapi", "laravel", "ruby on rails",

    # 🔹 Databases
    "mysql", "postgresql", "sqlite", "mongodb", "redis",
    "oracle", "cassandra", "firebase",

    # 🔹 Data Science & ML
    "machine learning", "deep learning", "nlp", "computer vision",
    "data analysis", "data mining", "feature engineering",
    "model evaluation", "statistics",

    # 🔹 ML Libraries
    "scikit-learn", "tensorflow", "keras", "pytorch",
    "xgboost", "lightgbm", "opencv", "nltk", "spacy",

    # 🔹 Data Tools
    "pandas", "numpy", "matplotlib", "seaborn", "plotly",
    "power bi", "tableau", "excel",

    # 🔹 DevOps & Cloud
    "aws", "azure", "gcp", "docker", "kubernetes",
    "ci/cd", "jenkins", "github actions", "terraform",

    # 🔹 APIs & Integration
    "rest api", "graphql", "api integration", "microservices",

    # 🔹 Version Control
    "git", "github", "gitlab", "bitbucket",

    # 🔹 Testing
    "unit testing", "pytest", "selenium", "jest",

    # 🔹 Mobile Development
    "android", "ios", "react native", "flutter",

    # 🔹 Cybersecurity
    "network security", "penetration testing", "ethical hacking",
    "cryptography", "owasp",

    # 🔹 Big Data
    "hadoop", "spark", "kafka", "hive",

    # 🔹 OS & Systems
    "linux", "unix", "windows server",

    # 🔹 Software Engineering Concepts
    "data structures", "algorithms", "oop", "system design",
    "design patterns", "scalability",

    # 🔹 Other Important Skills
    "deployment", "debugging", "performance optimization",
    "agile", "scrum"
]
    
    def exact_match(skill, text):
        return re.search(r'\b' + re.escape(skill) + r'\b', text)
    
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

    important_skills = [
        "python", "machine learning", "deep learning",
        "nlp", "tensorflow", "pytorch",
        "flask", "fastapi", "docker", "aws"
    ]

    # 🔥 Suggest only important missing skills
    for skill in missing_skills:
        if skill in important_skills:
            suggestions.append(f"Add projects using {skill}")

    # 🔥 Smart suggestions
    if "machine learning" not in resume_skills:
        suggestions.append("Include at least 2 Machine Learning projects")

    if "deployment" not in resume_skills:
        suggestions.append("Deploy your projects using Streamlit or Flask")

    if "nlp" not in resume_skills:
        suggestions.append("Add an NLP project (like chatbot or resume analyzer)")

    # ✅ If everything is good
    if len(suggestions) == 0:
        suggestions.append("Great! Your resume is well aligned with the job 🎯")

    return suggestions