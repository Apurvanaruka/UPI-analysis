import streamlit as st


# Connect me
st.sidebar.write("### Contact Me")
st.sidebar.write('[Gmail](%s)'%'https://mail.google.com/mail/u/0/?fs=1&to=apurvanaruka1@gmail.com&tf=cm')
st.sidebar.write('[Github](%s)' % 'https://github.com/apurvanaruka/')
st.sidebar.write('[Linkedin](%s)' % 'https://www.linkedin.com/in/apurva-naruka/')
st.sidebar.write('[upwork](%s)' % 'https://www.upwork.com/freelancers/~01add883bfa5bf8ef1?mp_source=share')


# Download cv
pdf_file_path = "static/Apurva Naruka cv.pdf"  # Path to your PDF file

with open(pdf_file_path, "rb") as file:
    pdf_data = file.read()

st.sidebar.download_button(
    label="Download CV",
    data=pdf_data,
    file_name="apurva_naruka_cv.pdf",
    mime="application/pdf"
)
# st.sidebar.download_button('Download CV', data="static/Apurva Naruka cv.pdf",)

# Profile Summary
st.title("Apurva Naruka's CV")

st.header("Profile Summary")
st.write("""
A highly motivated B.Tech student specializing in Artificial Intelligence and Data Science with a strong academic background and practical experience in machine learning, data analysis, and web development. Demonstrated skills through impactful projects and recognized achievements in national competitions. Proficient in Python, SQL, Power BI, and various data science tools.
""")

# Education
st.header("Education")
st.write("""
**B.Tech in Artificial Intelligence & Data Science**  
Modern Institute Of Technology And Research Center, 2021 - 2025  
CGPA: 8.50/10
""")

st.write("""
**Senior Secondary (XII), Science**  
Gyandeep Public Sr. Sec. School, Rajasthan Board of Secondary Education, 2021  
Percentage: 95.20%
""")

# Projects
st.header("Projects")

st.subheader("WhatsApp Chat Analysis")
st.write("""
**March 2024 - April 2024**  
- Analyzed WhatsApp chats for message frequency, activity timeline, word cloud, and individual activity in group chats.
- Tools: Python, Pandas, Matplotlib, Flask  
[Live Demo](https://whatsappchatanalysis-72l0.onrender.com/)
""")

st.subheader("Movie Recommendation System")
st.write("""
**March 2024**  
- Created a movie recommendation system using clustering algorithms on a dataset of 5000 Hollywood movies.
- Tools: Python, Scikit-learn, Flask  
[Live Demo](https://movie-recommendation-system-wz0a.onrender.com/)
""")


# Skills
st.header("Skills")
st.write("""
- **Programming Languages**: Python (Advanced), SQL (Intermediate)
- **Machine Learning**: Scikit-learn, TensorFlow, Keras (Intermediate)
- **Data Visualization**: Power BI, Tableau, Matplotlib, Seaborn (Intermediate)
- **Web Development**: Flask, Django (Intermediate)
- **Database Management**: MySQL, PostgreSQL (Intermediate)
- **Data Analysis & Processing**: Pandas, NumPy (Advanced)
- **Tools & Platforms**: Git, Docker, Jupyter Notebooks
""")

# Achievements
st.header("Achievements")
st.write("""
- **Winner**: Innovation, Design, and Entrepreneurship (IDE) Bootcamp Phase-2, organized by the Ministry of Education, Government of India.
- **Finalist**: Smart India Hackathon 2023
""")
