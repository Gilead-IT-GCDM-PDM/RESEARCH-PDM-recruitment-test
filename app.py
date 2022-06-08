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
    Output('pie_graph', 'children'),
    [
        Input('crew_type_dd', 'value'),
        Input('date_picker_range', 'start_date'),
        Input('date_picker_range', 'end_date')
    ]
)
def update_output_div(crew_type_dd, start_date, end_date):
    output = html.Div("{0} {1} {2}".format(crew_type_dd, start_date, end_date))
    df = sql_queries.get_pie_data(crew_type_dd, start_date, end_date)
    output = dcc.Graph(
        figure=px.pie(
            df,
            values='crew_count',
            names='crew_type',
            title='Crew of the Death Star'
        )
    )

    return output


if __name__ == '__main__':
    app.run_server(debug=True)
