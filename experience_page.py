import streamlit as st
from streamlit_lottie import st_lottie
import json

def experience():
    col1,col2 =st.columns(2)

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
                <h2>Experience</h2>
            </div>
        """, unsafe_allow_html=True)
    path = "Animation_exp.json"
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
        col1,col2 = st.columns([3,2])
        col1.markdown(""" 
            ### Credit Analyst Technology –– [BNP Paribas CIB](https://www.linkedin.com/company/bnpparibascorporateandinstitutionalbanking/) (PRESENT)
            - **Credit Committee Preparation and Presentation:** Prepared well-structured and detailed credit notes for strategic operations, including RCF refinancing and ABL facilities, managing an overall exposure of $1 billion, and ensuring thorough risk assessment.
            - **Financial and Sector Analysis:** Conducted in-depth studies on the economic performance and associated risks of companies in the technology sector (semiconductors, SaaS, IoT), considering market specifics and international regulations.
            - **Financing Structuring Contribution:** Worked on complex Leverage Buy-Out (LBO) transactions, assisting in the structuring of guarantees and optimizing financial arrangements.
            - **Risk Evaluation and Internal Ratings:** Participated in validating internal credit ratings, providing tailored recommendations aligned with the group's internal policies and strategic requirements.
            - **Process Automation and Optimization:** Developed VBA tools to streamline financial data analysis, reducing processing times for complex evaluations and enhancing operational efficiency.
            - **Cross-Team Collaboration:** Closely collaborated with teams in San Francisco to assess and structure complex international credit requests.
            - **Bond Issuance Participation:** Actively contributed to bond issuance projects in partnership with the Debt Capital Markets (DCM) and Leverage Finance teams, structuring and placing complex financings in the market.
                            """)
        col2.markdown("""
            **Tools:**

            - **Financial Analysis:** Capital IQ, Refinitiv
            - **Programming Languages:** Python, VBA
            - **Database Management:** SQL, SQLite
            - **Data Automation:** Excel VBA, Python scripts
            - **Market & Sector Reports:** Fixed Income (Investment Grade, High Yield), Corporate Credit
            - **Financial Products:** RCF, ABL, CDS, TRS, EQD, Term Loans, Bonds
            - **Collaboration:** Credit and Coverage San Francisco BNP CIB, Loan Capital Market, Leverage Finance, Global Trade Solutions
            """)
    with st.container():
        col1, col2 = st.columns([3, 2])
        col1.markdown("""
           ### Trader Assistant [La Française Asset Management](https://www.linkedin.com/company/lafrancaise-group/posts/?feedView=all) (Jun. 2022 - Dec. 2022)
    
           - **Process Automation:** Developed automated solutions in VBA for weekly reports, databases, and risk alerts on bonds via MarketAxess, streamlining reporting and enhancing the speed of risk analysis.
           - **Risk and Collateral Management:** Managed a broker quotation database using Python and SQLite, facilitating the evaluation of counterparties and valuation of collateral for transactions.
           - **Sectoral Analysis and Market Monitoring:** Compiled sectoral reports on the high-yield bond market, prepared performance summaries for high-yield funds, and created performance indicators for bond portfolios, improving strategic decision-making.
           - **Decision Support:** Assisted in the preparation of credit summaries for potential bond issuers, providing critical input to support the portfolio manager's investment decisions.
           """)
        col2.markdown(""" 
        **Tools:**
        
        - **Financial Analysis:** Capital IQ, Refinitiv, BQuant (Bloomberg)
        - **Programming Languages:** Python, VBA
        - **Database Management:** SQL, SQLite
        - **Data Automation:** Excel VBA, Python scripts
        - **Market & Sector Reports:** High Yield, Investment Grade Fixed Income, CDS Index Market
        - **Financial Products:** Bonds, Total Return Swap (TRS), Credit Default Swap (CDS)
        - **Collaboration:** Portfolio Management, Risk Management, Trading Desk, MarketAxess, Bloomberg  """)
    with st.container():
        col1, col2 = st.columns([3,2])

        col1.markdown("""
            ### Data Scientist –– [Alten S.A.](https://www.alten.com/)(Mar. 2021- Aug. 2021)
            - **Advanced Visualization Tools Development:** Designed and implemented an interactive visualization tool to analyze data science ontologies, improving accessibility and understanding of complex data for teams. This tool enabled users to better interpret and utilize large-scale data sets, driving more informed decision-making.
            - **AI Solutions Implementation:** Developed innovative IT solutions for the visualization and management of AI model databases, incorporating dynamic features to simplify usage for technical teams. These solutions enhanced data accessibility and provided real-time updates, contributing to improved workflows for data scientists and engineers.
            - **Analytical Process Optimization:** Deployed advanced technologies, including JavaScript and Node.js, to optimize the analytical process. Integrated real-time updates to ensure seamless data visualization and enhanced the efficiency of decision-making within the organization.
            """)
        col2.markdown("""
            **Tools:**
    
            - **Programming Languages:** JavaScript, Python, Node.js, Electron.js
            - **Version Control:** GitHub, GitLab
            - **Data Visualization:** JavaScript libraries (D3.js, etc.), Interactive UI/UX design
            - **Data Automation:** Python scripts, Node.js applications
            - **AI Solutions:** AI model database management tools
            - **Collaboration:** Technical Teams, Data Scientists, Engineers
            """)
    with st.container():
        col1, col2 = st.columns([3,2])
        col1.markdown("""
        ### Data Scientist –– [GAC Technology](https://www.gac-technology.com/) (May. 2020 - Jul. 2021)
        - **DAI Chatbot Development:** Initiated the development of an AI-based chatbot using neural networks to enhance customer support. Designed and implemented key features for interactive support, improving customer engagement and response time.
        - **Dataset Creation for Model Training:** Created a comprehensive dataset for training the neural network model, ensuring the data was representative of common customer inquiries and providing a solid foundation for the AI to learn from.
        - **Technology Monitoring and Chatbot Design:** Conducted ongoing research on advancements in neural networks and chatbot technologies, using Python, Keras, and TensorFlow to optimize the chatbot’s performance and integrate cutting-edge features. Continuously improved the model based on the latest industry trends.
            """)
        col2.markdown("""
        **Tools & Skills:**
    - **Programming Languages:** Python, SQL
    - **Libraries & Frameworks:** NLTK, scikit-learn, Pandas, NumPy
    - **Machine Learning Tools:** Classification, Forecasting
    - **Data Visualization Tools:** Tableau, Matplotlib, Seaborn, Power BI
    - **Other:** Data Cleaning, Statistical Analysis, Predictive Modeling """)



    # st.markdown()