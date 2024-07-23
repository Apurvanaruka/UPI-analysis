import streamlit as st
from preprocessor import *
import plotly.graph_objects as go


st.set_page_config(layout="wide")

st.title('UPI Transactions Analysis 📈')



def load_data():
    try:
        with st.expander('Upload Phonepe Statement pdf.'):
            pdf_file = st.file_uploader('Upload pdf file',['pdf'])
            return pdf_file
    except:
        return print('Error in pdf uploading')

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


def overall_statistics():
    st.write('### Overall Statistics')
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Total Amount", value=f"₹{total_amount(df):,.2f}")
        st.metric(label="Total Debit Amount", value=f"₹{total_debit_amount(df):,.2f}")
        st.metric(label="Total Credit Amount", value=f"₹{total_credit_amount(df):,.2f}")
        st.metric(label="Total Transactions", value=f"{len(df)}")

    with col2:
        st.metric(label="Maximum Credit Amount", value=f"₹{max_credit_amount(df):,.2f}")
        st.metric(label="Maximum Debit Amount", value=f"₹{max_debit_amount(df):,.2f}")
        st.metric(label="Average Transaction Amount", value=f"₹{avg_transaction_amount(df):,.2f}")

    with st.expander('### Detailed Transactions Data'):
        st.dataframe(df)


def amount_of_monthly_transactions():
    """Amount every Month show in a bar chart."""
    st.write('### Amount of Monthly Transactions')

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

    # Calculate the required statistics
    max_transaction_month = monthly_transaction.loc[monthly_transaction['total'].idxmax()]
    max_credit_month = monthly_transaction.loc[monthly_transaction['credit'].idxmax()]
    max_debit_month = monthly_transaction.loc[monthly_transaction['debit'].idxmax()]

    average_credit = monthly_transaction['credit'].mean()
    average_debit = monthly_transaction['debit'].mean()
    average_transaction = monthly_transaction['total'].mean()


    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])
    col11, col12 = tab1.columns(2)
    col21, col22 = tab2.columns(2)
    # Convert 'month' column to datetime objects for plotting
    monthly_transaction['month'] = pd.to_datetime(monthly_transaction['month'], format='%B-%Y')
    months_str = monthly_transaction['month'].dt.strftime('%B-%Y')

    # Create the figure
    fig = go.Figure()

    # Add debit transactions
    fig.add_trace(go.Line(
        x=months_str,
        y=monthly_transaction['debit'],
        name='Debit',
        marker_color='red',
        offsetgroup=0
    ))

    # Add total transactions
    fig.add_trace(go.Line(
        x=months_str,
        y=monthly_transaction['total'],
        name='Total',
        marker_color='skyblue',
        offsetgroup=1
    ))

    # Add credit transactions
    fig.add_trace(go.Line(
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
    col11.plotly_chart(fig)

    # Start building the Streamlit app
    with col12:
        st.write("### 📅 Maximum Transactions Month")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Month", value=max_transaction_month['month'])
        with col2:
            st.metric(label="Total Amount", value=f"₹{max_transaction_month['total']:,}")
        st.write("### 💰 Maximum Credit in a Month")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Month", value=max_credit_month['month'])
        with col2:
            st.metric(label="Credit Amount", value=f"₹{max_credit_month['credit']:,}")
        st.write("### 💸 Maximum Debit in a Month")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Month", value=max_debit_month['month'])
        with col2:
            st.metric(label="Debit Amount", value=f"₹{max_debit_month['debit']:,}")

    with col21:
        st.write(monthly_transaction)

    with col22:
        st.write("### 📉 Average Statistics")
        st.metric(label="Average Credit", value=f"₹{average_credit:,.2f}")
        st.metric(label="Average Debit", value=f"₹{average_debit:,.2f}")
        st.metric(label="Average Total Transactionst", value=f"₹{average_transaction:,.2f}")


def frequently_transations_amount():
    st.write('### Transations Frequency Amount')
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

    mostly_transaction_frequncy = amount_count[:5]

    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.bar_chart(amount_count[:20], x='amount', y='frequency')
        with col2:
            st.write("### :sparkles: Top 5 Transactions Amount")
            st.table(mostly_transaction_frequncy)
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.write("## 📋 Data table")
            st.write(amount_count)
        with col2:
            # Select top 5 categories
            top_10 = amount_count.head(10)

            # Sum the rest of the categories
            others = pd.DataFrame({
                'amount': ['Other'],
                'frequency': [amount_count['frequency'].iloc[10:].sum()]
            })

            # Combine top 5 and 'Other'
            final_data = pd.concat([top_10, others])

            # Create a pie chart using Plotly's graph_objects
            fig = go.Figure(data=[go.Pie(labels=final_data['amount'], values=final_data['frequency'],textinfo='label+percent')])
            fig.update_layout(title_text='💥 Pie Chart')

            # Display the pie chart
            st.plotly_chart(fig)


def frequently_transations_person():
    st.write('### Transations Frequency Person')
    name_set = set(df['name'].tolist())
    name_list = []
    freq_list = []
    total_amount_list = []
    for name in name_set:
        name_list.append(name)
        freq_list.append(df['name'].tolist().count(name))
        total_amount_list.append(sum(df[df['name'] == name]['amount']))

    amount_count = pd.DataFrame({'name': name_list,
                                 'frequency': freq_list,
                                 'total_amount' : total_amount_list
                                 }).sort_values(by='frequency',
                                  ascending=False).reset_index(drop=True)
    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.bar_chart(amount_count[:20], x='name', y='frequency')
        with col2:
            st.write('### :sparkles: Top 5 Transactions Frequency')
            st.table(amount_count[:5])
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.write('### 📄Data Table')
            st.write(amount_count)
        with col2:
            st.write('### 🚀 Maximum Amount Transaction')
            st.write(amount_count.sort_values(by='total_amount',ascending=False)[:5])
def no_of_monthly_transactions():
    """Show number of transactions per month in bar chart."""
    st.write('### No of monthly Transactions')

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


    # Calculate the required statistics
    max_transaction_month = monthly_transaction_len.loc[monthly_transaction_len['total_len'].idxmax()]
    max_credit_month = monthly_transaction_len.loc[monthly_transaction_len['credit_len'].idxmax()]
    max_debit_month = monthly_transaction_len.loc[monthly_transaction_len['debit_len'].idxmax()]

    average_credit = monthly_transaction_len['credit_len'].mean()
    average_debit = monthly_transaction_len['debit_len'].mean()
    average_transaction = monthly_transaction_len['total_len'].mean()

    tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
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

            st.plotly_chart(fig)

        with col2:
            st.write("### 📅 Maximum No. of Transactions in Month")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Month", value=max_transaction_month['month'])
            with col2:
                st.metric(label="Total Transactions", value=f"{max_transaction_month['total_len']:,}")
            st.write("### 💰 Maximum Credit Transactions in a Month")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Month", value=max_credit_month['month'])
            with col2:
                st.metric(label="Credit Transactions", value=f"{max_credit_month['credit_len']:,}")
            st.write("### 💸 Maximum Debit Transaction in a Month")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Month", value=max_debit_month['month'])
            with col2:
                st.metric(label="Debit Transactions", value=f"{max_debit_month['debit_len']:,}")

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.write(monthly_transaction_len)

        with col2:
            st.write("### 📉 Average Statistics in Month")
            st.metric(label="Average Credit Transactions", value=f"{int(average_credit)}")
            st.metric(label="Average Debit Transactions", value=f"{int(average_debit)}")
            st.metric(label="Average Total Transactions", value=f"{int(average_transaction)}")

def show_category():
    labels = df['label'].unique()
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Number of transcations per Category")
        values = df['label'].value_counts()
        tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])
        with tab1:
                # Use `hole` to create a donut-like pie chart
                fig = go.Figure(data=[go.Pie(labels=labels,values=values,textinfo='label+percent',hole=.4)])
                st.plotly_chart(fig)
        with tab2:
            st.write(pd.DataFrame({'Total Transactiona':values}))
    with col2:
        st.write("### Amount of transcations per Category")
        values = [ df[df['label'] == label ]['amount'].sum() for label in labels ]
        tab1, tab2 = st.tabs(['📊 Graph', '📄 Data'])
        with tab1:
            # Use `hole` to create a donut-like pie chart
            fig = go.Figure(data=[go.Pie(labels=labels,values=values,textinfo='label+percent',hole=.4)])
            st.plotly_chart(fig)
        with tab2:
            st.write(pd.DataFrame({'Category':labels,'Total Amount':values}))

def show_tutorial():
    st.write("### How to get phonepe Statement pdf file?")
    st.write('Open Phonepe Application in your smartphone.')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('## Step 1')
        st.write("Open phonepe app.Navigate to History section")
        st.image('images/step1.jpeg',width=250)
    with col2:
        st.write('## Step 2')
        st.write("Click on Download Statment.")
        st.image('images/step2.jpeg',width=250)
    with col3:
        st.write('## Step 3')
        st.write("Select time period. Click on procced.")
        st.image('images/step3.jpeg',width=250)
    with col4:
        st.write('## Step 4')
        st.write("View pdf file. And verify it is correct.")
        st.image('images/step5.jpeg',width=250)
    

pdf_file=load_data()

if pdf_file is not None:
    text = pdf_to_text(pdf_file)
    transactions = parse_text(text)
    dataframe = convert_to_dataframe(transactions)
    df=preprocessor(dataframe)
    overall_statistics()
    show_category()
    amount_of_monthly_transactions()
    no_of_monthly_transactions()
    frequently_transations_amount()
    frequently_transations_person()

else:
    show_tutorial()

# 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
