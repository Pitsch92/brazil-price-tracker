import streamlit as st
import pandas as pd
import plotly.express as px
import re

# Load data
df = pd.read_csv('full_table_2025-05-26.csv')

# Extract storage size using regex
df['Storage'] = df['Produto'].str.extract(r'(\d+GB|\d+TB)', expand=False)

# Analysis 1: Most and least expensive models
max_row = df.loc[df['Preço'].idxmax()]
min_row = df.loc[df['Preço'].idxmin()]

# Analysis 2: Average price by model
avg_price_by_model = df.groupby('Produto')['Preço'].mean().sort_values(ascending=False)

# Analysis 3: Price trend for a selected model
model_options = df['Produto'].unique()
selected_model = st.selectbox("Select a model for price trend:", model_options)
trend = df[df['Produto'] == selected_model].sort_values('Data')

# Analysis 4: Model listing counts
model_counts = df['Produto'].value_counts()

# Analysis 5: Top 5 most expensive models per day
df['rank'] = df.groupby('Data')['Preço'].rank(method='first', ascending=False)
top5_per_day = df[df['rank'] <= 5].sort_values(['Data', 'Preço'], ascending=[True, False])

# Analysis 6: Price spread by storage size
spread = df.groupby('Storage').agg(
    min_preco=('Preço', 'min'),
    max_preco=('Preço', 'max'),
    avg_preco=('Preço', 'mean'),
    count=('Preço', 'count')
).reset_index().sort_values('avg_preco', ascending=False)

# ---- Streamlit Layout ----

st.title("iPhone 16 Price Analysis Dashboard 📱")

st.header("1. Most and Least Expensive Models")
st.write("**Most expensive:**", max_row['Produto'], f"R${max_row['Preço']:.2f}")
st.write("**Least expensive:**", min_row['Produto'], f"R${min_row['Preço']:.2f}")

st.header("2. Average Price by Model")
st.dataframe(avg_price_by_model.reset_index().rename(columns={'Preço': 'Average Price'}))

st.header("3. Price Trend for Selected Model")
fig1 = px.line(trend, x='Data', y='Preço', title=f'Price Trend: {selected_model}')
st.plotly_chart(fig1)

st.header("4. Model Listing Frequency")
st.bar_chart(model_counts)

st.header("5. Top 5 Most Expensive Models per Day")
st.dataframe(top5_per_day[['Data', 'Produto', 'Preço']])

st.header("6. Price Spread by Storage Size")
st.dataframe(spread)

st.caption("Data source: Magazine Luiza iPhone 16 listings")
