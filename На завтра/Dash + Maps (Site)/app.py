import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Создаем приложение Dash
app = dash.Dash(__name__)

# Загружаем данные для карты (пример)
data = pd.DataFrame({
    "Country": ["Russia", "USA", "China", "India", "Brazil"],
    "Population": [144.5, 327.2, 1393, 1369, 209.5],
    "GDP": [1.7, 21.4, 14.3, 2.6, 1.8],
    "Life Expectancy": [71, 79, 76, 69, 75],
    "Continent": ["Europe", "North America", "Asia", "Asia", "South America"]
})

# Создаем интерактивную карту с использованием Plotly Express
fig = px.scatter_geo(data, locations="Country", locationmode="country names",
                     color="Continent", hover_name="Country",
                     size="Population", projection="natural earth")

# Разметка веб-страницы
app.layout = html.Div([
    html.H1("Мировая карта с Dash и Plotly"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
