import streamlit as st



def load_data():
    try:
        with st.expander('Load Data'):
            pdf_file = st.file_uploader('Upload pdf file',['pdf'])
            return pdf_file
    except:
        return print('error in pdf uploading')

# Functions
def total_amount(df):
    return df['amount'].sum()

def total_debit_amount(df):
    return df[df['type'] == 'DEBIT']['amount'].sum()

def total_credit_amount(df):
    return df[df['type'] == 'CREDIT']['amount'].sum()

def max_credit_amount(df):
    return df[df['type'] == 'CREDIT']['amount'].max()

def max_debit_amount(df):
    return df[df['type'] == 'DEBIT']['amount'].max()

def avg_transaction_amount(df):
    return df['amount'].mean()
