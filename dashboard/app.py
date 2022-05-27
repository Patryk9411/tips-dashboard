from typing import List

import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

from components.filtering import tips_range_slider

# import z naszych components i graphs
from components.static import navbar
from graphs.templates import bar_day, sex_pie, time_scatter

# from data.external import tips_df  # tutaj pobieranie data setu z externela w data

# tworzymy aplikacje
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# dodajemy naglowek - najlepiej przejrzec dokumentacje biblioteki


# layout - wyglad dashboardu
app.layout = dbc.Container(
    [
        navbar,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.B("Select the range of tips: "), width=2),
                dbc.Col(tips_range_slider(), width=10),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(id="time-scatter-col", children=time_scatter()),
                dbc.Col(id="sex-pie-col", children=sex_pie()),
                dbc.Col(id="bar-day-col", children=bar_day()),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("time-scatter-col", "children"),
    Output("sex-pie-col", "children"),
    Output("bar-day-col", "children"),
    Input("tips-range-slider", "value"),
)
def adjust_tips_range(tips_range: List[float]):
    return (time_scatter(tips_range), sex_pie(tips_range), bar_day(tips_range))


# zabezpiczenie, zeby przez przypadek nie odpalic serwera
if __name__ == "__main__":
    app.run_server(
        port=8062,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
