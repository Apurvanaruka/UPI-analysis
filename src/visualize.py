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
