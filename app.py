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
                        dcc.DatePickerRange(
                            id='date_picker_range',
                            min_date_allowed=date(2022, 5, 1),
                            max_date_allowed=date(2022, 6, 20),
                            start_date=date(2022, 5, 1),
                            end_date=date(2022, 6, 20)
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
# FIGURE OUT THE CALLBACK PARAMETERS
)
def update_output_div(crew_type_dd, start_date, end_date):
    # Your biggest hint on if filters are working
    output = html.Div("{0} {1} {2}".format(crew_type_dd, start_date, end_date))

    # 1 Get the data
    # 2 Build a plotly pie graph, count crew by type

    return output


if __name__ == '__main__':
    app.run_server(debug=True)
