import streamlit as st
from load_data import load_data
from preprocessor import *
from visualize import *


st.title('UPI Transactions Analysis')
pdf_file=load_data()

df = None

def total_amount(df):
    monthly_transaction = pd.DataFrame(columns=['month', 'credit', 'debit', 'total'])
    
    for date in df['datetime']:
        month_year = date.strftime('%B-%Y')
        credits = df[(df['datetime'].dt.strftime('%B-%Y') == month_year) & (df['type'] == 'CREDIT')]['amount'].sum()
        debits = df[(df['datetime'].dt.strftime('%B-%Y') == month_year) & (df['type'] == 'DEBIT')]['amount'].sum()
        total = credits + debits
        
        # Append row to monthly_transaction DataFrame
        monthly_transaction = monthly_transaction._append({
            'month': month_year,
            'credit': credits,
            'debit': debits,
            'total': total
        }, ignore_index=True)
    
    # Display monthly_transaction DataFrame in Streamlit
    st.write(monthly_transaction)
    
    # Convert 'month' column to datetime objects for plotting
    monthly_transaction['month'] = pd.to_datetime(monthly_transaction['month'], format='%B-%Y')
    months = monthly_transaction['month']
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_width = 5
    
    # Plot debit transactions
    ax.bar(months - pd.DateOffset(days=5), monthly_transaction['debit'], width=bar_width, label='Debit', align='center',color='red')
    
    # Plot total transactions
    ax.bar(months, monthly_transaction['total'], width=bar_width, label='Total', align='center',color='skyblue')
    
    # Plot credit transactions
    ax.bar(months + pd.DateOffset(days=5), monthly_transaction['credit'], width=bar_width, label='Credit', align='center',color='green')
    
    ax.set_title('Transaction Amounts Over Time')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.legend()
    ax.grid(axis='y')
    plt.xticks(rotation=45)
    
    # Display the plot in Streamlit
    st.pyplot(fig)



text = pdf_to_text(pdf_file)
transactions = parse_text(text)
dataframe = convert_to_dataframe(transactions)
df=preprocessor(dataframe)



st.write(f'Total no of transactions = {len(df)}')
st.write(f'Average Amount of every transaction ₹{sum(df.amount)//len(df)}')

st.write(df)







total_amount(df)
show_monthly_transaction(df)
show_type(df)


