import streamlit as st



def load_data():
    try:
        with st.expander('Load Data'):
            pdf_file = st.file_uploader('Upload pdf file',['pdf'])
            return pdf_file
    except:
        return print('error in pdf uploading')
