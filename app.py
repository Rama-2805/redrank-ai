import streamlit as st
import pandas as pd

from src.dashboard import get_dashboard_stats
from src.gap_analysis import gap_analysis
from src.candidate_compare import compare_candidates
from src.jd_generator import generate_jd
from src.resume_parser import extract_resume_text
from src.resume_matcher import extract_skills
from src.resume_scorer import score_resume
from src.explain_candidate import explain_candidate
from src.recruiter_ai import ask_recruiter
from src.match_breakdown import calculate_match

st.set_page_config(
    page_title="RedRank AI",
    layout="wide"
)

st.title("🚀 RedRank AI")
st.subheader("Intelligent Candidate Discovery")

# Resume Upload

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

resume_text = ""
skills = []
jd_skills = []

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    resume_text = extract_resume_text(
        uploaded_file
    )

    skills = extract_skills(
        resume_text
    )

    st.subheader(
        "Detected Skills"
    )

    st.write(
        ", ".join(skills)
    )

    st.subheader(
        "Resume Preview"
    )

    st.text_area(
        "Resume Content",
        resume_text[:2000],
        height=200
    )

    if st.button(
        "🤖 Generate Job Description"
    ):

        with st.spinner(
            "Generating AI Job Description..."
        ):

            st.session_state["generated_jd"] = generate_jd(
                resume_text
            )

# Generated JD Section

if "generated_jd" in st.session_state:

    st.subheader(
        "🤖 AI Generated Job Description"
    )

    jd = st.text_area(
        "Generated JD",
        st.session_state["generated_jd"],
        height=300
    )

    jd_skills = extract_skills(
        st.session_state["generated_jd"]
    )

    gap = gap_analysis(
        skills,
        jd_skills
    )

    st.subheader(
        "🎯 JD Gap Analysis"
    )

    st.metric(
        "JD Match",
        f"{gap['score']}%"
    )

    st.write(
        "✅ Matched Skills"
    )

    st.write(
        ", ".join(
            gap["matched"]
        )
    )

    st.write(
        "❌ Missing Skills"
    )

    st.write(
        ", ".join(
            gap["missing"]
        )
    )

else:

    jd = st.text_area(
        "Paste Job Description",
        height=250
    )
# Rank Candidates

if st.button("Rank Candidates"):

    df = pd.read_csv(
        "submission_top100.csv"
    )
    stats = get_dashboard_stats(df)

    st.subheader("📊 Recruiter Analytics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Average Score",
        stats["avg_score"]
    )

    c2.metric(
        "Highest Score",
        stats["max_score"]
    )

    c3.metric(
        "Lowest Score",
        stats["min_score"]
    )
    st.session_state["df"] = df

    st.success(
        "Top Candidates Found"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Top Match",
        round(df.iloc[0]["score"], 2)
    )

    c2.metric(
        "Candidates",
        len(df)
    )

    c3.metric(
        "Top Role",
        "AI/ML"
    )

    c4.metric(
        "Status",
        "Ready"
    )

    st.divider()

    for rank, (_, row) in enumerate(
        df.head(10).iterrows(),
        start=1
    ):

        info = explain_candidate(
            row["candidate_id"]
        )

        match = calculate_match(
            info,
            row["score"]
        )

        resume_match = 0

        if uploaded_file:

            resume_match = score_resume(
                skills,
                info["skills"]
            )

        st.markdown(
            f"# 🏆 Rank #{rank}"
        )

        st.markdown(
            f"""
### {info['title']}

**Candidate ID:** {row['candidate_id']}

**Experience:** {info['experience']} Years

**Match Score:** {round(row['score'],2)}

**Resume Match:** {resume_match}%

**Key Skills:** {', '.join(info['skills'])}

**GitHub Activity:** {info['github']}

**Interview Completion:** {round(info['interview_rate']*100)}%

**Open To Work:** {'✅ Yes' if info['open_to_work'] else '❌ No'}
"""
        )

        mc1, mc2, mc3, mc4 = st.columns(4)

        mc1.metric(
            "Skills Match",
            f"{match['skills']}%"
        )

        mc2.metric(
            "Experience Match",
            f"{match['experience']}%"
        )

        mc3.metric(
            "Title Match",
            f"{match['title']}%"
        )

        mc4.metric(
            "Recruiter Signals",
            f"{match['recruiter']}%"
        )

        st.write(
            f"Overall Match: {match['overall']}%"
        )

        st.progress(
            min(
                int(match["overall"]),
                100
            )
        )

        st.write(
            f"Resume Match Score: {resume_match}%"
        )

        st.progress(
            min(
                int(resume_match),
                100
            )
        )

        if st.button(
            f"🤖 Analyze Candidate #{rank}",
            key=row["candidate_id"]
        ):

            prompt = f"""
Candidate Title: {info['title']}
Experience: {info['experience']} years
Skills: {', '.join(info['skills'])}
GitHub Activity: {info['github']}
Interview Completion Rate: {info['interview_rate']}

Act as a senior recruiter.

Provide:
1. Candidate Summary
2. Strengths
3. Weaknesses
4. Hiring Recommendation

Keep it concise.
"""

            with st.spinner(
                "Analyzing candidate..."
            ):

                answer = ask_recruiter(
                    prompt
                )

            st.success(
                "AI Analysis Complete"
            )

            st.write(
                answer
            )

        st.divider()

        

    st.header("⚔️ Candidate Comparison")

    top1 = explain_candidate(
        df.iloc[0]["candidate_id"]
    )

    top2 = explain_candidate(
        df.iloc[1]["candidate_id"]
    )

    comparison = compare_candidates(
        top1,
        top2
    )

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Candidate #1")

        st.write(
            top1["title"]
        )

        st.write(
            f"Experience: {top1['experience']} Years"
        )

        st.write(
            f"GitHub: {top1['github']}"
        )

    with c2:

        st.subheader("Candidate #2")

        st.write(
            top2["title"]
        )

        st.write(
            f"Experience: {top2['experience']} Years"
        )

        st.write(
            f"GitHub: {top2['github']}"
        )

    st.success(
        f"🏆 Winner: {comparison['winner']}"
    )

# AI Recruiter Copilot

# AI Recruiter Copilot

st.markdown("---")

st.header(
    "🤖 AI Recruiter Copilot"
)

question = st.text_input(
    "Ask a question about candidates"
)

if st.button("Ask AI"):

    with st.spinner("Analyzing..."):

        if "df" in st.session_state:

            top_candidate = explain_candidate(
                st.session_state["df"].iloc[0]["candidate_id"]
            )

            prompt = f"""
Candidate Title: {top_candidate['title']}
Experience: {top_candidate['experience']}
Skills: {', '.join(top_candidate['skills'])}
GitHub Activity: {top_candidate['github']}
Interview Completion: {top_candidate['interview_rate']}

Question:
{question}

Answer ONLY using the candidate data above.
"""

            answer = ask_recruiter(
                prompt
            )

        else:

            answer = ask_recruiter(
                question
            )

    st.success(
        "AI Response"
    )

    st.write(
        answer
    )