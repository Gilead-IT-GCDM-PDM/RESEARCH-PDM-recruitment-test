from dash import Dash, dcc, html, Input, Output
from datetime import date
import dash_bootstrap_components as dbc
import plotly.express as px
import sql_queries

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src=app.get_relative_path(
                            "/assets/death_star_logo.png"),
                        style={"height": "30px"},
                    ),
                    width=1
                ),
                dbc.Col(
                    html.H5("Death Star Crew Dashboard"),
                    width=6
                )
            ],
            style={"margin": "5px"}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div("Crew Type"),
                        dcc.Dropdown(
                            options=[
                                {'label': 'All', 'value': 'All'},
                                {'label': 'Crew', 'value': 'Crewmen'},
                                {'label': 'VIP', 'value': 'VIP'},
                            ],
                            value='All',
                            id="crew_type_dd"
                        )
                    ],
                    width=1
                ),
                dbc.Col(
                    [
                        html.Div("Start Date"),
                        dcc.DatePickerSingle(
                            id='date_picker',
                            min_date_allowed=date(2022, 5, 1),
                            max_date_allowed=date(2022, 6, 20),
                            # initial_visible_month=date(2022, 5, 1),
                            date=date(2022, 6, 20)
                        ),
                    ],
                    width=4
                ),
            ],
            style={"margin": "5px"}
        ),
        dbc.Row(
            dbc.Col(
                html.Div("Pie Gaph", id="pie_graph")
            ),
            style={"margin": "5px"}
        ),
    ]
)


@app.callback(
    # Determine what you need in your callbacks
)
def update_output_div(crew_type_dd, pick_date):
    output = html.Div("{0} {1}".format(crew_type_dd, pick_date))
    df = sql_queries.get_pie_data(crew_type_dd, pick_date)
    # Determine how to build the pie graph and put it to the output

    return output


if __name__ == '__main__':
    app.run_server(debug=True)
