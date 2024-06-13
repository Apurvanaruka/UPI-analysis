import streamlit as st
from load_data import load_data
from preprocessor import *
from visualize import *


st.write('upi analysis')
pdf_file=load_data()

df = None

if st.button('Analyis Data'):
    if not pdf_file:
        st.warning('Please Upload PDF file!')
    else:
        text = pdf_to_text(pdf_file)
        transactions = parse_text(text)
        dataframe = convert_to_dataframe(transactions)
        df=preprocessor(dataframe)
        st.write(df)
        show_monthly_transaction(df)