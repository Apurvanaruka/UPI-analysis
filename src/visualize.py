import matplotlib.pyplot as plt
import streamlit as st

def show_monthly_transaction(df):
    df['month'] = df['datetime'].dt.to_period('M')
    # Group by month and sum the amounts
    monthly_data = df.groupby('month')['amount'].sum().reset_index()

    # Convert 'month' back to datetime for plotting
    monthly_data['month'] = monthly_data['month'].dt.to_timestamp()

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly_data['month'], monthly_data['amount'], marker='o', linestyle='-')
    ax.set_title('Monthly Amounts')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot in Streamlit
    st.title('Monthly Amounts Plot')
    st.pyplot(fig)


def show_type(df):
    # st.bar_chart(data=df,x=df['datetime'].timestamp,y=df['amount'],color=df['type'])
    # Plotting with Matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df['datetime'], df['amount'])
    ax.set_title('Value over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(axis='y')  # Add gridlines only for y-axis

    # Display the plot in Streamlit
    st.pyplot(fig)
