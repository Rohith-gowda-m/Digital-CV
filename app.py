from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rohith Gowda M"
PAGE_ICON = ":wave:"
NAME = "Rohith Gowda M"
DESCRIPTION = """
Highly motivated professional with experience 
in business process improvement, data analysis 
and project management. Proven ability to 
identify opportunities for process improvement 
and develop strategies for implementation. 
Adept in utilizing analytics to develop business 
insights and drive new product development.
"""
EMAIL = "rgrohith21@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rohith-gowda-m-146248172/",
    "GitHub": "https://github.com",
    "Publication": "https://www.researchgate.net/profile/Dr-Madhusudhan-3/publication/331950405_In_silico_Screening_and_Identification_of_Potent_Antiprotozoal_Drugs_Against_Aquaporin_Protein_of_Nosema_Species_Infecting_Silkworm_and_Honey_Bee/links/5c9472eb92851cf0ae8eb98e/In-silico-Screening-and-Identification-of-Potent-Antiprotozoal-Drugs-Against-Aquaporin-Protein-of-Nosema-Species-Infecting-Silkworm-and-Honey-Bee.pdf",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
st.sidebar.image(profile_pic, width=230)
st.sidebar.title(NAME)
st.sidebar.write(DESCRIPTION)
# st.sidebar.write("📫", EMAIL)
st.sidebar.markdown(
    '📫 <a href="mailto:rgrohith21@gmail.com?subject=Requesting%20CV&body=I%20am%20interested%20in%20your%20CV,%20please%20forward%20me%20the%20same." style="color:blue;">rgrohith21@gmail.com 🔗</a>.',
    unsafe_allow_html=True
)

# --- SOCIAL LINKS ---
st.sidebar.write('\n')
st.sidebar.title("SOCIAL LINKS")
for platform, link in SOCIAL_MEDIA.items():
    st.sidebar.write(f"[{platform}]({link})")

# --- REACHING OUT ---
st.sidebar.write('\n')
st.sidebar.markdown(
    'If you are pleased with my profile, reach out to me via' 
)
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: center;">
        <a href="mailto:rgrohith21@gmail.com?subject=Requesting%20CV&body=I%20am%20interested%20in%20your%20CV,%20please%20forward%20me%20the%20same." style="color:blue;">
            <button style="background-color: #0077b5; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">Email</button>
        </a>
        <span style="margin: 0 10px;">or</span>
        <a href="https://www.linkedin.com/in/rohith-gowda-m-146248172/" target="_blank">
            <button style="background-color: #0077b5; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">LinkedIn</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


# --- MAIN CONTENT ---
st.write('\n')
st.subheader("PROJECTS")
for platform, link in PROJECTS.items():
    if link:
        st.write(f"[{platform}]({link})")
    else:
        st.write(platform)

# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("QUALIFICATIONS")
st.write(
    """
- ✔️ Indian Institute of Technology, Kharagpur
-     April 2019 - March 2021                  
-     Master of Technology, Agricultaral Biotechnology - CGPA : 8.5
                                 

- ✔️ JSS University, Mysuru (SJCE)
-     April 2015 - 2019                              
-     Bachelor of Engineering, Biotechnology  -  CGPA : 9.0
                                        
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("SKILLS")
st.write(
    """
- 👩‍💻 Programming : Python, SQL, SPARK
- 📊 Data Visualization : PowerBI, Tableau, MS Excel
- 📚 Tools : Azure, Databricks, Data Factory, Synapse, Alteryx, Fabric, Hue, Looker_Studio, Azure Blob Storage
- 🗄️ Technical :  Confluence, Bitbucket, Jira, Git, Scrum, Agile, SAFe, SDLC, CI/CD
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("WORK HISTORY")
st.write("---")

# --- JOB 1
st.write("🚧", "**Business Analyst | Tata Consultancy Services**")
st.write("December 2022 – Current")
st.write(
    """
- ► Strong business acumen with the ability to translate business needs into data solutions 
influenced by BABOK principle and guidelines (CBAP), Communication skills, 
Leadership and Team Management, Critical thinking, Innovative solution deployment, 
streamlining business process, Decision making and Data Governance. 
- ► Analyzed business processes to identify improvements and efficiency gains 
across six projects in medical equipment, pharmaceuticals, vision care, and 
surgical vision sectors.
- ► Document requirements from stakeholders (APAC, EMEA, NA) and business 
leader to support business process models, user stories, functional 
specifications and drive data-driven decisions.
- ► Provided detailed walkthroughs of BI reports and dashboards for B2C and B2B 
operations, aiding strategic planning.
- ► Designed a comprehensive model from source to UI for 10 countries across APAC 
and EMEA. 
- ► Participated in strategic planning for future initiatives, contributing to budget, effort 
estimation, and goal setting for the next financial year. 

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Engineer | Tata Consultancy Services**")
st.write("April 2022 – December 2023")
st.write(
    """
- ► Engineered and maintained scalable, efficient data pipelines for collecting, processing, 
and storing large datasets, resulting in a 30% reduction in data processing time. 
- ► Designed and implemented robust data architecture solutions, ensuring data integrity, 
security, and accessibility, which led to increase in data reliability. 
- ► Established best practices for data flow management in collaboration with IT, resulting 
in decrease in system downtime and led to improvement in user satisfaction ratings 
among internal stakeholders. 
- ► Collaboratively converted the existing SQL codebase to PySpark, reducing end-to-end 
processing time by 40% through efficient data transformation processes.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Tata Consultancy Services**")
st.write("July 2021 – March 2022")
st.write(
    """
- ► Implemented data visualization techniques that reduced visuals load time by 30% and developed simplified visuals to effectively communicate findings to stakeholders.
- ► Designed over 7 financial dashboards that defines key performance indicators (KPIs) and functional visuals to visualize business process to derive actionable insights from trends, outliers and patterns.
- ► Enhanced business decision-making by implementing time series forecasting, resulting in increase in prediction accuracy, and identified key opportunities for prescriptive analytics to improve operational efficiency.

"""
)
