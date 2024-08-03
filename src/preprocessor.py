import pandas as pd
import re
import PyPDF2
from datetime import datetime
import streamlit as st
from utils import *


def pdf_to_text(pdf_file):
    # Open the PDF file in read-binary mode
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Initialize an empty string to store the text
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text


def is_valid_date_format(date_str):
    pattern = r"^[A-Z][a-z]{2} \d{2}, \d{4}$"
    return bool(re.match(pattern, date_str))


# reshape list
def reshape(lines):
  reshaped_lines = []
  for i in range(0,len(lines)):
    if 'Page' in lines[i]:
      i+=6
    if is_valid_date_format(lines[i]):
      reshaped_lines.append(lines[i:i+9])
      i+=9
  return reshaped_lines


# Step 2: Parse the extracted text
def parse_text(text):
    transactions = []
    lines = text.split('\n')
    return reshape(lines[6:])

# Step 3: Convert to DataFrame and Export
def convert_to_dataframe(transactions):
    df = pd.DataFrame(transactions)
    return df

@st.cache_data
def preprocessor(df):
  df.columns = ['date','time','type','amount','name','transaction_id','utr_no','type_','account_no']
  df=df.drop('type_',axis=1)
  df['time'] = pd.to_datetime(df['time'], format='%I:%M %p').dt.time
  df['date'] = pd.to_datetime(df['date'], format='%b %d, %Y')
  df.insert(0,'datetime',df.apply(lambda row: datetime.combine(row['date'].date(), row['time']), axis=1))
  df['amount'] = df['amount'].str.replace('₹', '').str.replace(',', '').astype(float)
  df['utr_no'] = df['utr_no'].str.replace('UTR No. ', '')
  df['name'] = df['name'].str.replace(r'^(Paid to|Received from|Transfer to)\s', '', regex=True)
  df['transaction_id'] = df['transaction_id'].str.replace('Transaction ID ', '')

  df['label'] = df['name'].map(classify_name)
  df=df.drop(['date','time'],axis=1)
  return df

# def export_to_excel(df, excel_path):
#     df.to_excel(excel_path, index=False)

# def export_to_json(df, json_path):
#     df.to_json(json_path, orient='records', indent=4)

# Main script
# text = extract_text_from_pdf(pdf_path)
# transactions = parse_text(text)
# dataframe = convert_to_dataframe(transactions)
# df=preprocessor(dataframe)
# export_to_excel(df, "transactions.xlsx")
# export_to_json(df, "transactions.json")
