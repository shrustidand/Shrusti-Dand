import streamlit as st

st.set_page_config(
    page_title="Shrusti Dand",
    page_icon="👩‍💼",
    layout="wide"
)

st.title("Shrusti Dand")
st.subheader(
    "Aspiring HR Professional | Talent Acquisition & People Management Enthusiast"
)

st.write("""
Results-oriented PGDM HR student with practical experience in
recruitment, talent acquisition, onboarding, and human resource operations.
""")

st.header("About Me")

st.write("""
Passionate HR professional pursuing PGDM in Human Resources.
Experienced in recruitment, candidate screening, onboarding,
HR operations, communication, leadership, and team management.
""")

st.header("Education")

st.markdown("""
### PGDM in Human Resources
Sasmira's Business School, Mumbai

June 2025 – April 2027

### Bachelor of Business Administration (Hons.) in HR
S.K. Somaiya College, Mumbai

August 2022 – April 2025

**CGPI: 9.67**
""")

st.header("Skills")

skills = [
    "Recruitment",
    "Talent Acquisition",
    "Candidate Screening",
    "Interview Coordination",
    "HR Operations",
    "Communication",
    "Leadership",
    "Teamwork",
    "Advanced Excel"
]

st.write(", ".join(skills))

st.header("Contact")

st.write("📧 shrustidand@gmail.com")
st.write("📱 7285857598")
st.write("📍 Mumbai, Maharashtra, India")