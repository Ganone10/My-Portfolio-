import streamlit as st
import json
from streamlit_lottie import st_lottie

def projects():
    col1, col2 = st.columns(2)

    # col1.markdown("## Experience")
    with col1:
        st.markdown("""
                <style>
                .centered {
                    display: flex;
                    align-items: center;
                    height: 100%;
                    margin-top: 200px; /* Adjust this value as needed */
                }
                </style>
                <div class="centered">
                    <h2>Projects </h2>
                </div>
            """, unsafe_allow_html=True)
    path = "Animation_girl.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:
        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )

    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            with st.container(border=True):


                # Displaying the title of the project
                st.title("Finance Tool with StreamLit")

                # Displaying the description
                st.markdown("""
                **Description:**
                This project aims to develop an interactive dashboard using Streamlit, a Python library for creating web applications for data science and machine learning projects. The dashboard will provide users with an intuitive interface to explore and visualize data, perform analysis, and interact with machine learning models.
        
                - **Data Visualization:** Utilizes Streamlit's built-in components to create interactive charts, plots, and visualizations for exploring data.
                - **User Interaction:** Allows users to interact with the dashboard through widgets such as sliders, dropdowns, buttons, and text inputs to customize data visualization and analysis.
                - **Integration with Machine Learning Models:** Incorporates machine learning models into the dashboard to provide real-time predictions or analysis based on user input.
                - **Deployment:** Enables easy deployment of the dashboard as a web application using Streamlit's deployment options or platforms such as Heroku, AWS, or Azure..
                """)

                # Displaying the tools used
                st.markdown("""
                **Tools Used:**
                
                 **Python 3.x**,
                 **Streamlit**,
                 **pandas**,
                 **numpy**,
                 **scikit-learn (if integrating machine learning models)**,
                 **matplotlib and/or seaborn (for data visualization)** 
                """)
                st.markdown(""" """)


                c1,c2,c3,c4 = st.columns(4)
                #c1.markdown("""**[Link to app](https://insightful-data-explorer-001.streamlit.app)**  """)
                #c2.markdown("""**[GitHub](https://github.com/archanags001/Insightful-Data-Explorer)**""")
                #c3.markdown("""**[LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7220172770226102272/)** """)
                #c4.markdown("""**[X](https://x.com/streamlit/status/1814406829075542029)**""")
                rc1,rc2 = st.columns(2)
                rc1.markdown("""**[Github](https://github.com/Ganone10/Finance-Tool-with-StreamLit)**""")
                rc2.markdown("""**[Streamlit community](https://streamlit.io/)**""")


        with col2:
            with st.container(border=True):
                # Displaying the title of the project
                st.title("Portfolio Strategy with CAC40 Stocks")
                # Displaying the description
                st.markdown("""
                **Description:**
                This project, we aim to design a portfolio investment strategy focusing on CAC40 stocks. The primary objective is to construct a benchmark portfolio based on the market capitalization of these stocks. Subsequently, we will explore more advanced strategies in a later part of the project.

                - **Data Analysis:** Perform historical statistical analysis of CAC40 stocks' performance, with a focus on key financial ratios, market trends, and volatility metrics. This analysis will serve as a comprehensive introduction to portfolio management and provide insights into risk-return frameworks, such as the Value at Risk (VaR) and Risk-Reward (Sharpe Ratio), laying the foundation for advanced portfolio strategies.
                - **Sample Datasets:** Access sample datasets containing historical data for CAC40 stocks, allowing users to explore key financial indicators and test portfolio management strategies without requiring their own data..
                """)
                st.markdown(""" """)


                # Displaying the tools used
                st.markdown("""
                **Tools Used:**

                **R**, **Rstudio**,  **Excel**, **Pandas**
                
                """)
                st.markdown(""" """)
                st.markdown(""" """)
                st.markdown(""" """)
                st.markdown(""" """)


                c1, c2 = st.columns(2)
                #c1.markdown("""**[Link to app](https://chat-with-data-gemini.streamlit.app)**  """)
                c1.markdown("""**[GitHub](https://github.com/Ganone10/Projet-Intro-to-DS)**""")

                
                
                


        with col1:
            with st.container(border=True):
                # Displaying the title of the project
                st.title("Sentiment Analysis of Financial News Articles")

                # Displaying the description
                st.markdown("""
                **Description:**
                This project utilizes machine learning techniques in Python to analyze the sentiment of financial news articles. It aims to provide insights into the sentiment (positive, negative, or neutral) of news articles related to the financial market.

                - **Sentiment Analysis:** Utilizes natural language processing (NLP) techniques to perform sentiment analysis on financial news articles.
                - **Data Preprocessing:** Includes data preprocessing steps such as tokenization, removing stopwords, punctuation, and special characters, and converting text to lowercase.
                - **Machine Learning Models:** Implements machine learning models for sentiment analysis, including pre-trained models and custom models trained on financial news datasets.
                - **Evaluation Metrics:** Evaluates model performance using standard evaluation metrics such as accuracy, precision, recall, and F1-score.
                - **Web Scraping (Optional):** Provides an option to scrape financial news articles from online sources for real-time sentiment analysis.
                """)
                st.markdown(""" """)



                # Displaying the tools used
                st.markdown("""
                **Tools Used:**

                **Python 3.x**, **pandas**, **numpy**, **scikit-learn**, **nltk**
                """)
                st.markdown(""" """)
                st.markdown(""" """)
                st.markdown(""" """)
                

                # Adding the GitHub link
                st.markdown("""**[GitHub](https://github.com/Ganone10/ML-Article-Sentiment/tree/master)**""")

        with col2:
            with st.container(border=True):
                # Displaying the title of the project
                st.title("Credit Analysis Dashboard with DCF Simulation (Ongoing Project)")

                # Displaying the description
                st.markdown("""
                **Description:**
                This ongoing project aims to develop an interactive credit analysis dashboard using Streamlit, a Python library for creating web applications. The dashboard will provide users with the ability to explore and visualize key financial and credit ratios of publicly traded companies, alongside performing Discounted Cash Flow (DCF) simulations for growth projections. The goal is to offer insights into both creditworthiness and company valuation, helping to support more informed credit decision-making.
                - **Data Visualization:** The dashboard will feature interactive charts and visualizations, built with **Streamlit**, to display financial metrics such as **Debt-to-Equity ratio**, **Interest Coverage ratio**, and other credit-related indicators. Users will be able to customize views for deeper analysis.
                - **User Interaction:** The platform will support dynamic user interaction through various widgets, such as **sliders**, **dropdown menus**, **buttons**, and **text inputs**, enabling customization of data visualization and analysis parameters, including adjusting assumptions for the DCF model.
                - **Integration with DCF Simulation Model:** A **DCF simulation model** will be integrated into the platform, allowing users to model future growth and project a company's value based on input parameters. This feature will allow for scenario analysis and understanding the impact of different assumptions on credit evaluation.
                - **Real-Time Financial Analysis:** Users will be able to explore and analyze **live** or **historical financial data** of public stocks, assessing a company’s financial health using up-to-date financial statements and relevant credit ratios.
                - **Deployment:** The application will be easily deployable as a web app using **Streamlit's built-in deployment options** or other cloud platforms like **Heroku**, **AWS**, or **Azure** for broader accessibility.
                """)
                st.markdown(""" """)


                # Displaying the tools used
                st.markdown("""
                **Tools Used:**

                **Python 3.x**, **Streamlit**, **pandas**, **numpy**, **scikit-learn**, **matplotlib**, **yinance**
                """)
                st.markdown(""" """)


                # Adding the GitHub link
                st.markdown("""**[GitHub](https://github.com/archanags001/coding_challenge/blob/main/Coding_challenge_.ipynb)**""")

        with col1:
            with st.container(border=True):
                # Displaying the title of the project
                st.title("Portfolio Explorer ")

                # Displaying the description
                st.markdown("""
                **Description:**
                The Portfolio Explorer is a Streamlit-based application designed to present a comprehensive and interactive personal portfolio. Key features include:

                - **Intro Page:** A dynamic introduction offering a professional overview.
                - **Resume Page:** A viewable and downloadable resume for quick access to detailed professional information.
                - **Experience Page:** An organized display of work experience, skills, and accomplishments.
                - **Projects Page:** A showcase of notable projects, including descriptions, technologies used, and links to repositories.
                - **Testimonial Page:** A collection of feedback and testimonials from clients and colleagues, highlighting accomplishments and collaborations.
                - **Contact Page:** An integrated contact form for easy communication and inquiries.
                """)

                # Displaying the tools used
                st.markdown("""
                **Tools Used:**

                **Python** , **Streamlit**
                """)
                st.markdown(""" """)

                c1, c2, c3, c4, c5 = st.columns(5)


                # Adding the GitHub link
                c1.markdown("""**[Link to app](https://portfolio-archana.streamlit.app)**  """)
                c2.markdown("""**[GitHub](https://github.com/archanags001/Portfolio/tree/main)**""")



