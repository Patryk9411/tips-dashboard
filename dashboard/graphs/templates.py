from typing import List

import plotly.express as px
from dash import dcc
from data.external import tips_df


def time_scatter(tips_range: List[float] = None) -> dcc.Graph:
    df = tips_df()
    if tips_range is not None:
        df = df.loc[df.tip.between(*tips_range)]
    return dcc.Graph(
        id="time_scatter",
        figure=px.scatter(
            df,
            x="total_bill",
            y="tip",
            color="time",
            title="Does tips depends on the time of day?",
            # hover_data, to co sie pokaze jak najedziemy na punkt na wykresie - tooltip
        ),
    )


def sex_pie(tips_range: List[float] = None) -> dcc.Graph:
    df = tips_df()
    if tips_range is not None:
        df = df.loc[df.tip.between(*tips_range)]
    return dcc.Graph(
        id="sex_pie",
        figure=px.pie(
            df,
            values="tip",
            names="sex",
            title="Does tips depends on gender?",
        ),
    )


def bar_day(tips_range: List[float] = None) -> dcc.Graph:
    df = tips_df()
    if tips_range is not None:
        df = df.loc[df.tip.between(*tips_range)]
    return dcc.Graph(
        id="bar_day",
        figure=px.bar(
            df.groupby("day")["tip"].mean().reset_index(),
            x="day",
            y="tip",
            title="Does tips depends on the day of the week?",
        ),
    )
