import dash_bootstrap_components as dbc
from dash import html

tips_logo = "https://media-cldnry.s-nbcnews.com/image/upload/streams/2013/June/130611/6C7835371-130611-tippng-505p.jpg"
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=tips_logo, height="80px")),
                    dbc.Col(dbc.NavbarBrand("Tips dashboard", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
        ]
    ),
    color="dark",
    dark="True",
)
