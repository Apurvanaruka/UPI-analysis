import streamlit as st

def load_data():
    try: 
        pdf_file = st.sidebar.file_uploader('Upload pdf file',['pdf'])
        return pdf_file
    except:
        return None
