import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, Input, Output
import re

# Load your CSV file
df = pd.read_csv("full_table_2025-05-26.csv")

# Extract storage size (e.g., "128GB", "1TB") from product name
df['Storage'] = df['Produto'].str.extract(r'(\d+GB|\d+TB)', expand=False)

# Analysis 1: Most and least expensive models
max_row = df.loc[df['Preço'].idxmax()]
min_row = df.loc[df['Preço'].idxmin()]

# Analysis 2: Average price by model
avg_price_by_model = df.groupby('Produto')['Preço'].mean().sort_values(ascending=False).reset_index()

# Analysis 3: Price trend for a selected model (interactive)
model_options = df['Produto'].unique()

# Analysis 4: Model listing counts
model_counts = df['Produto'].value_counts().reset_index()
model_counts.columns = ['Produto', 'Count']

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

# Build Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("iPhone 16 Price Analysis Dashboard (Dash)", style={'textAlign': 'center'}),

    html.H2("1. Most and Least Expensive Models"),
    html.Div([
        html.P(f"Most expensive: {max_row['Produto']} (R${max_row['Preço']:.2f})"),
        html.P(f"Least expensive: {min_row['Produto']} (R${min_row['Preço']:.2f})")
    ]),

    html.H2("2. Average Price by Model"),
    dash_table.DataTable(
        data=avg_price_by_model.to_dict('records'),
        columns=[{"name": i, "id": i} for i in avg_price_by_model.columns],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    ),

    html.H2("3. Price Trend for Selected Model"),
    dcc.Dropdown(
        id='model-dropdown',
        options=[{'label': m, 'value': m} for m in model_options],
        value=model_options[0],
        style={'width': '80%'}
    ),
    dcc.Graph(id='trend-graph'),

    html.H2("4. Model Listing Frequency"),
    dcc.Graph(
        figure=px.bar(model_counts.head(20), x='Produto', y='Count', title="Top 20 Most Listed Models")
    ),

    html.H2("5. Top 5 Most Expensive Models per Day"),
    dash_table.DataTable(
        data=top5_per_day[['Data', 'Produto', 'Preço']].to_dict('records'),
        columns=[{"name": i, "id": i} for i in ['Data', 'Produto', 'Preço']],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    ),

    html.H2("6. Price Spread by Storage Size"),
    dash_table.DataTable(
        data=spread.to_dict('records'),
        columns=[{"name": i, "id": i} for i in spread.columns],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    ),
    html.Br(),
    html.P("Data source: Magazine Luiza iPhone 16 listings", style={'fontStyle': 'italic'}),
])

# Callback for interactive price trend graph
@app.callback(
    Output('trend-graph', 'figure'),
    Input('model-dropdown', 'value')
)
def update_trend(selected_model):
    trend = df[df['Produto'] == selected_model].sort_values('Data')
    fig = px.line(trend, x='Data', y='Preço', title=f'Price Trend: {selected_model}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)