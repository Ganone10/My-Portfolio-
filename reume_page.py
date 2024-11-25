import streamlit as st
from streamlit_pdf_viewer import pdf_viewer



def resume():
    with open("CV Alexis Andreani English 2024.pdf", "rb") as pdf_file:
        document = pdf_file.read()

    st.markdown("""
            <style>
            .stDownloadButton button {
                background-color: #1E9E35 !important;
                color: white !important;
            }
            </style>
            """, unsafe_allow_html=True)


    st.download_button(
                label="Download Resume",
                key="download_button",
                file_name="CV Alexis Andreani English 2024.pdf",
                data=document,
                help="Click to download.",
            )
    with st.container():
        st.markdown(
            """
            <style>
            .stContainer > div {
                width: 55%;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        pdf_viewer("CV Alexis Andreani English 2024.pdf")
