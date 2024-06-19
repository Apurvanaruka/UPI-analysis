import streamlit as st
from preprocessor import *
from visualize import *
from utils import *


st.title('UPI Transactions Analysis 📈')
pdf_file=load_data()

df = None

def amount_of_monthly_transactions():
    '''Amount every Month show in a bar chart.'''
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
    
    tab1,tab2 = st.tabs(['📊 Graph','📄 Data'])

    # Convert 'month' column to datetime objects for plotting
    monthly_transaction['month'] = pd.to_datetime(monthly_transaction['month'], format='%B-%Y')
    months = monthly_transaction['month']
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_width = 8
    
    # Plot debit transactions
    ax.bar(months - pd.DateOffset(days=8), monthly_transaction['debit'], width=bar_width, label='Debit', align='center',color='red')
    
    # Plot total transactions
    ax.bar(months, monthly_transaction['total'], width=bar_width, label='Total', align='center',color='skyblue')
    
    # Plot credit transactions
    ax.bar(months + pd.DateOffset(days=8), monthly_transaction['credit'], width=bar_width, label='Credit', align='center',color='green')
    
    ax.set_title('Transaction Amounts Over Time')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.legend()
    ax.grid(axis='y')
    plt.xticks(rotation=45)
    
    # Display the plot in Streamlit
    tab1.pyplot(fig)
    tab2.write(monthly_transaction)

def no_of_monthly_transactions():
    """show number of transactions per month in bar char"""

    monthly_transaction_len = pd.DataFrame(columns=['month', 'credit_len', 'debit_len', 'total_len'])
    for date in df['datetime']:
        month_year = date.strftime('%B-%Y')
        credits_len = len(df[(df['datetime'].dt.strftime('%B-%Y') == month_year) & (df['type'] == 'CREDIT')])
        debits_len = len(df[(df['datetime'].dt.strftime('%B-%Y') == month_year) & (df['type'] == 'DEBIT')])
        total_len = credits_len + debits_len
        monthly_transaction_len = monthly_transaction_len._append({
                'month': month_year,
                'credit_len': credits_len,
                'debit_len': debits_len,
                'total_len': total_len
            }, ignore_index=True)
    tab1,tab2 = st.tabs(['📊 Graph','📄 Data'])
    
    # Convert 'month' column to datetime objects for plotting
    monthly_transaction_len['month'] = pd.to_datetime(monthly_transaction_len['month'], format='%B-%Y')
    months = monthly_transaction_len['month']
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_width = 8
    # Plot debit transactions
    ax.bar(months - pd.DateOffset(days=8), monthly_transaction_len['debit_len'], width=bar_width, label='Debit', align='center',color='red')
    # Plot total transactions
    ax.bar(months, monthly_transaction_len['total_len'], width=bar_width, label='Total', align='center',color='skyblue')
    # Plot credit transactions
    ax.bar(months + pd.DateOffset(days=8), monthly_transaction_len['credit_len'], width=bar_width, label='Credit', align='center',color='green')
    ax.set_title('Transaction Amounts Over Time')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.legend()
    ax.grid(axis='y')
    plt.xticks(rotation=45)
    
    # Display the plot in Streamlit
    tab1.pyplot(fig)    
    tab2.write(monthly_transaction_len)

def frequently_transations_amount():
    amount_set = set(df['amount'].tolist())

    amount_list = []
    freq_list = []
    for amount in amount_set:
        amount_list.append(amount)
        freq_list.append(df['amount'].tolist().count(amount))
    amount_count = pd.DataFrame({'amount':amount_list, 'frequency':freq_list}).sort_values(by='frequency',ascending=False).reset_index(drop=True)
    tab1,tab2 = st.tabs(['📊 Graph','📄 Data'])
    # fig, ax = plt.subplots(figsize=(12, 8))
    # ax.bar(x=amount_count['amount'],height=amount_count['frequency'])
    # tab1.pyplot(fig)
    tab1.bar_chart(amount_count[:20],x='amount',y='frequency')
    tab2.write(amount_count)

text = pdf_to_text(pdf_file)
transactions = parse_text(text)
dataframe = convert_to_dataframe(transactions)
df=preprocessor(dataframe)

st.write(f'Total no of transactions = {len(df)}')
st.write(f'Average Amount of every transaction ₹{sum(df.amount)//len(df)}')

with st.expander('DataFrame'):
    st.write(df)





amount_of_monthly_transactions()
no_of_monthly_transactions()
frequently_transations_amount()

# show_monthly_transaction(df)
# show_type(df)


