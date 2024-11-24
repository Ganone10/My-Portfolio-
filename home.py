import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os
from streamlit_lottie import st_lottie
import requests
import json
from reume_page import resume
from experience_page import experience
from upwork_page import feedbackRating
from project_page import projects
from contact_form import contact


# Get the PORT from environment variable and convert to an integer
port = int(os.getenv("PORT", 8501))  # Default to 8501 if PORT is not set

st.set_page_config(page_title="Alexis Andreani", page_icon="🌐")




def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',

              unsafe_allow_html=True)
def aboutMe():
    #col1, col2 = st.columns(2)
    col1 = st.columns(1)
    full_name = "Alexis Andreani"
    info = {'Intro': "Credit Analyst"}

    with col1[0]:
        st.markdown("<h2 style='text-align: center; '>Alexis Andreani | Credit Analyst & Data Enthusiast | CS Engineer, MSc in Finance</h2>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        .center-text {
        text-align: justify;
        }
        </style>
        
        - **About me:**
        <div class="justify-text">
        My name is Alexis Andreani and I am a dedicated Credit Analyst with a strong foundation in finance, credit, and equity markets. and a background in data science with an engineering degree in Computer Science.
        My professional journey has equipped me with a unique blend of analytical skills and technological expertise, allowing me to deliver comprehensive credit assessments and innovative solutions that drive impactful decisions.
        In my role at BNP Paribas CIB, I have successfully prepared credit memos for new requests and annual reviews, including underwriting RCF refinances for investment-grade clients managing a portfolio with a total exposure of more than $1Bn. 
        My focus on the technology sector has allowed me to conduct in-depth financial and industry analyses, evaluating credit ratings and managing credit risk portfolios for U.S. clients.
        Complementing my credit expertise, my background in data science and automation has empowered me to streamline processes through VBA-based tools and manage broker quotation databases using Python and SQLite. 
        I take pride in designing dynamic financial projection models and developing automated reporting solutions that enhance decision-making efficiency.
        I hold an MSc in Finance from EM Lyon Business School, specializing in Market & Quantitative Finance, and have pursued advanced studies in Applied Mathematics and Computer Engineering. 
        Passionate about coding and continuous learning, I leverage my technical skills to explore innovative solutions in both finance and technology.
        
        </div>
        """, unsafe_allow_html=True)

        st.markdown(""" """) #Give some space between description and interests

        c1,c2 =st.columns([1,2])
        c1.markdown("""
        <style>
        .center-text {
        text-align: justify;
        }
        </style>
        
        **Interest:**<br>
        <div class="justify-text">
        <ul>
        <li>Market Finance</li>
        <li>Private Debt</li>
        <li>Credit Analysis</li>
        <li>Data Analysis</li>
        <li>Technology & Innovation</li>
        <li>IA & Data Science</li>
        <ul>
        </div>
                       
        """, unsafe_allow_html=True)
        c2.markdown("""
        <style>
        .center-text {
        text-align: justify;
        }
        </style>
        
        **Education:**<br>
        <div class="justify-text">
        <ul>
            <li><strong>MSc in Finance</strong> - EM Lyon Business School (2021 - 2023)<br>
            Specialization: Market & Quantitative Finance
            </li>
            <li><strong>Computer Science Engineering Degree</strong> - ENSIIE (2018 - 2021)<br>
            Focus: Data Science, Machine Learning, and AI
            </li>
            <li><strong>CPGE (Mathematics and Physics)</strong> - Lycée Militaire Aix-en-Provence (2016 - 2018)<br>
            Focus: Science and Mathematics
            </li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(""" """)

        d1, d2 = st.columns(2)
        d1.markdown("""
        
        **My links:**<br>
        **- [GitHub](https://github.com/Ganone10)**<br>
        **- [LinkedIn](https://www.linkedin.com/in/alexisandreani/)**<br>
                       
        """, unsafe_allow_html=True)


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get the base64 string of the image
logo_base64 = get_base64_image("Alexis_Image.jpg")

# Logo styling
logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""

# Display logo in the sidebar
st.sidebar.markdown(logo_html, unsafe_allow_html=True)
with st.sidebar:
    # Other sidebar elements
    # st.sidebar.image("logo_image.png", width=200, use_column_width=True)
    # Option menu in sidebar
    pages = ["About me", "Resume", "Experience",  "Projects", "Contact"]
    nav_tab_op = option_menu(
        menu_title="Alexis Andreani",
        options=pages,
        icons=['person-fill', 'file-text', 'briefcase', 'folder', 'envelope'],
        menu_icon="cast",
        default_index=0,
    )
# Main content of the app
if nav_tab_op == "About me":
    aboutMe()

elif nav_tab_op == "Resume":
    resume()
elif nav_tab_op == "Experience":
    experience()
elif nav_tab_op == "Projects":
    projects()
elif nav_tab_op == "Contact":
    contact()


