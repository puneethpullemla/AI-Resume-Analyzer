import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("src"))

from src.extractor import extract_text_from_pdf
from src.cleaner import clean_text
from src.similarity import compute_similarity
from src.skills import skill_match_score, generate_suggestions

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")


st.title("🚀 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste Job Description Here")

if st.button("Analyze Resume"):

    if uploaded_file is None or job_description.strip() == "":
        st.warning("Please upload resume and paste job description.")
        st.stop()

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")

    if not resume_text:
        st.error("Could not extract text from PDF.")
        st.stop()

    resume_clean = clean_text(resume_text)[:1000]
    job_clean = clean_text(job_description)

    # Scores
    semantic_score = compute_similarity(resume_clean, job_clean)
    semantic_score = min(semantic_score, 0.95)
    semantic_percent = semantic_score * 100

    skill_score, matched_skills, missing_skills, resume_skills = skill_match_score(resume_clean, job_clean)

    final_score = (semantic_percent * 0.6) + (skill_score * 0.4)

    suggestions = generate_suggestions(missing_skills, resume_skills)

    # ✅ UI starts here
    st.subheader("📊 Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Semantic Score", f"{round(semantic_percent, 2)}%")
    col2.metric("Skill Score", f"{round(skill_score, 2)}%")
    col3.metric("ATS Score", f"{round(final_score, 2)}%")

    st.progress(int(final_score))

    st.subheader("🧠 Skills Analysis")

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("### ✅ Matched Skills")
        st.write(matched_skills if matched_skills else "No skills matched")

    with col5:
        st.markdown("### ❌ Missing Skills")
        st.write(missing_skills if missing_skills else "No missing skills")

    st.subheader("💡 Suggestions")

    if suggestions:
        for s in suggestions:
            st.write("👉", s)
    else:
        st.success("Great! Your resume matches well 🎉")