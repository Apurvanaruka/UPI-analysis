import streamlit as st
from load_data import load_data
from preprocessor import *
from visualize import *


st.write('upi analysis')
pdf_file=load_data()

df = None


def total_amount(df):


    # df['datetime'] = pd.to_datetime(df['datetime'])
    # df['amount'] = df['amount'].str.replace(',', '').astype(float)
    # Streamlit app
    st.title('Transaction Amounts Over Time')

    # Range selector for datetime
    min_date = df['datetime'].min().date()
    max_date = df['datetime'].max().date()
    start_date, end_date = st.slider(
        "Select date range",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
        format="YYYY-MM-DD"
    )

    # Convert the selected dates to datetime for filtering
    start_datetime = pd.to_datetime(start_date)
    end_datetime = pd.to_datetime(end_date)

    # Filter DataFrame based on selected date range
    filtered_df = df[(df['datetime'] >= start_datetime) & (df['datetime'] <= end_datetime)]

    # Plotting with Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot DEBIT transactions in red
    debit_df = filtered_df[filtered_df['type'] == 'DEBIT']
    ax.bar(debit_df['datetime'], debit_df['amount'], color='red', label='DEBIT')

    # Plot CREDIT transactions in green
    credit_df = filtered_df[filtered_df['type'] == 'CREDIT']
    ax.bar(credit_df['datetime'], credit_df['amount'], color='green', label='CREDIT')

    ax.set_title('Transaction Amounts Over Time')
    ax.set_xlabel('Datetime')
    ax.set_ylabel('Amount')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    ax.legend()
    ax.grid(axis='y')

    # Display the plot in Streamlit
    st.pyplot(fig)


text = pdf_to_text(pdf_file)
transactions = parse_text(text)
dataframe = convert_to_dataframe(transactions)
df=preprocessor(dataframe)
st.write(df)
total_amount(df)
show_monthly_transaction(df)
show_type(df)

