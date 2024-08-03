import streamlit as st

st.set_page_config(layout="wide")

# create globle data variable
try:
    with st.sidebar.expander('Upload Phonepe Statement pdf.'):
        st.session_state.pdf_file = st.file_uploader('Upload pdf file',['pdf'])
    
except:
    st.sidebar.write('Error in pdf uploading')

pg = st.navigation([
    st.Page("home.py",title="Home",icon=":material/home:"),
    st.Page("about_me.py",title="About Me", icon="🙂")])
pg.run()

