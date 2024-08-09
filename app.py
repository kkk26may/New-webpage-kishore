import streamlit as st
import pandas as pd

# Create a Streamlit app
st.title('WhatsApp Chat Analyzer')

# Load the parsed data
df = pd.read_csv('/content/whatsapp_chat_parsed.csv')

# Display the DataFrame
st.dataframe(df)

# Create a line chart of messages per day
st.line_chart(df['day'], df['Message'])

# Create a pie chart of messages per sender
st.pie_chart(df['Username'], df['Message'])

# Create a bar chart of messages per hour
st.bar_chart(df['hour'], df['Message'])
