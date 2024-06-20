import streamlit as st
from preprocessor import *
from utils import *
import plotly.graph_objects as go



st.title('UPI Transactions Analysis 📈')
pdf_file=load_data()
text = pdf_to_text(pdf_file)
transactions = parse_text(text)
dataframe = convert_to_dataframe(transactions)
df=preprocessor(dataframe)

with st.expander('DataFrame'):
    st.write(df)

st.write('### Overall Statistics')
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Total Amount", value=f"₹{total_amount(df):,.2f}")
    st.metric(label="Total Debit Amount", value=f"₹{total_debit_amount(df):,.2f}")
    st.metric(label="Total Credit Amount", value=f"₹{total_credit_amount(df):,.2f}")

with col2:
    st.metric(label="Maximum Credit Amount", value=f"₹{max_credit_amount(df):,.2f}")
    st.metric(label="Maximum Debit Amount", value=f"₹{max_debit_amount(df):,.2f}")
    st.metric(label="Average Transaction Amount", value=f"₹{avg_transaction_amount(df):,.2f}")

st.write('### Detailed Transactions Data')
st.dataframe(df)


def amount_of_monthly_transactions():
    """Amount every Month show in a bar chart."""
    monthly_transaction = pd.DataFrame(columns=['month', 'credit', 'debit', 'total'])
    for date in df['datetime']:
        month_year = date.strftime('%B-%Y')
        credit = df[(df['datetime'].dt.strftime('%B-%Y') == month_year) & (df['type'] == 'CREDIT')]['amount'].sum()
        debits = df[(df['datetime'].dt.strftime('%B-%Y') == month_year) & (df['type'] == 'DEBIT')]['amount'].sum()
        total = credit + debits

        # Append row to monthly_transaction DataFrame
        monthly_transaction = monthly_transaction._append({
            'month': month_year,
            'credit': credit,
            'debit': debits,
            'total': total
        }, ignore_index=True)
        monthly_transaction.drop_duplicates(ignore_index=True, inplace=True)

    # Display monthly_transaction DataFrame in Streamlit

    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])

    # Convert 'month' column to datetime objects for plotting
    monthly_transaction['month'] = pd.to_datetime(monthly_transaction['month'], format='%B-%Y')
    months_str = monthly_transaction['month'].dt.strftime('%B-%Y')

    # Create the figure
    fig = go.Figure()

    # Add debit transactions
    fig.add_trace(go.Bar(
        x=months_str,
        y=monthly_transaction['debit'],
        name='Debit',
        marker_color='red',
        offsetgroup=0
    ))

    # Add total transactions
    fig.add_trace(go.Bar(
        x=months_str,
        y=monthly_transaction['total'],
        name='Total',
        marker_color='skyblue',
        offsetgroup=1
    ))

    # Add credit transactions
    fig.add_trace(go.Bar(
        x=months_str,
        y=monthly_transaction['credit'],
        name='Credit',
        marker_color='green',
        offsetgroup=2
    ))

    # Update the layout
    fig.update_layout(
        title='Transaction Amounts Over Time',
        xaxis_title='Month',
        yaxis_title='Amount',
        barmode='group',
        bargap=0.15,
        bargroupgap=0.1,
        xaxis_tickangle=-45,
        legend_title='Transaction Type',
        width=1000,
        height=500,
    )

    # Display the plot in Streamlit
    tab1.plotly_chart(fig)
    tab2.write(monthly_transaction)


def frequently_transations_amount():
    amount_set = set(df['amount'].tolist())
    amount_list = []
    freq_list = []
    for amount in amount_set:
        amount_list.append(amount)
        freq_list.append(df['amount'].tolist().count(amount))
    amount_count = pd.DataFrame({
        'amount': amount_list,
        'frequency': freq_list
    }).sort_values(by='frequency', ascending=False).reset_index(drop=True)
    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])
    # fig, ax = plt.subplots(figsize=(12, 8))
    # ax.bar(x=amount_count['amount'],height=amount_count['frequency'])
    # tab1.pyplot(fig)
    tab1.bar_chart(amount_count[:20], x='amount', y='frequency')
    tab2.write(amount_count)


def frequently_transations_person():
    amount_set = set(df['name'].tolist())
    amount_list = []
    freq_list = []
    for amount in amount_set:
        amount_list.append(amount)
        freq_list.append(df['name'].tolist().count(amount))
    amount_count = pd.DataFrame({'name': amount_list,
                                 'frequency': freq_list}).sort_values(by='frequency',
                                  ascending=False).reset_index(drop=True)
    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])
    # fig, ax = plt.subplots(figsize=(12, 8))
    # ax.bar(x=amount_count['amount'],height=amount_count['frequency'])
    # tab1.pyplot(fig)
    tab1.bar_chart(amount_count[:20], x='name', y='frequency')
    tab2.write(amount_count)


def no_of_monthly_transactions():
    """Show number of transactions per month in bar chart."""

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
        monthly_transaction_len.drop_duplicates(ignore_index=True, inplace=True)

    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])

    # Convert 'month' column to datetime objects for plotting
    monthly_transaction_len['month'] = pd.to_datetime(
        monthly_transaction_len['month'],
        format='%B-%Y')
    months_str = monthly_transaction_len['month'].dt.strftime('%B-%Y')

    # Create the figure
    fig = go.Figure()

    # Add debit transactions
    fig.add_trace(go.Bar(
        x=months_str,
        y=monthly_transaction_len['debit_len'],
        name='Debit',
        marker_color='red',
        offsetgroup=0,
    ))

    # Add total transactions
    fig.add_trace(go.Bar(
        x=months_str,
        y=monthly_transaction_len['total_len'],
        name='Total',
        marker_color='skyblue',
        offsetgroup=1
    ))

    # Add credit transactions
    fig.add_trace(go.Bar(
        x=months_str,
        y=monthly_transaction_len['credit_len'],
        name='Credit',
        marker_color='green',
        offsetgroup=2
    ))

    # Update the layout
    fig.update_layout(
        title='Number of Transactions Over Time',
        xaxis_title='Month',
        yaxis_title='Number of Transactions',
        barmode='group',
        bargap=0.15,
        bargroupgap=0.1,
        xaxis_tickangle=-45,
        legend_title='Transaction Type',
        width=1000,  # Increase the width of the plot
        height=500  # Increase the height of the plot
    )

    # Display the plot in Streamlit
    tab1.plotly_chart(fig)
    tab2.write(monthly_transaction_len)


amount_of_monthly_transactions()
no_of_monthly_transactions()
frequently_transations_amount()
frequently_transations_person()
