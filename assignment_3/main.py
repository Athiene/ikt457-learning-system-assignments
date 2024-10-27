# Import packages
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

SF_x = [1, 2, 3]
SF_y = [1, 2, 3]

# App layout
app.layout = html.Div(
    [
        # Graph
        dcc.Graph(
            figure={
                'data': [
                    {'x': SF_x, 'y': SF_y, 'type': 'bar', 'name': 'SF'},
                    {'x': SF_x, 'y': SF_y, 'type': 'bar', 'name': 'Montreal'},
                ],
                'layout': {
                    'title': 'Interactive Stationary Distribution Bar Chart'
                }
            }
        ),

        # Slider for s
        dcc.Markdown('''#### Slider: s'''),
        dcc.Slider(1, 25, 0.1, value=12, id="s-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Div(id='s-output', style={'marginTop': 20}),

        # Slider for P(L|Y)
        dcc.Markdown('''#### Slider: P(L|Y)'''),
        dcc.Slider(0, 1, 0.01, value=0.5, id="P(L|Y)-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Div(id='P(L|Y)-output', style={'marginTop': 20}),

        # Slider for P(Y)
        dcc.Markdown('''#### Slider: P(Y)'''),
        dcc.Slider(0, 1, 0.01, value=0.5, id="P(Y)-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Div(id='P(Y)-output', style={'marginTop': 20}),

        # Slider for P(-L|-Y)
        dcc.Markdown('''#### Slider: P(-L|-Y)'''),
        dcc.Slider(0, 1, 0.01, value=0.5, id="P(-L|-Y)-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Div(id='P(-L|-Y)-output', style={'marginTop': 20}),

    ], style={'border': '10px solid #ddd', 'padding': '10px', 'marginTop': '20px', "margin-left": "15%",
              "margin-right": "15%"},
)


# Callbacks to update the output for each slider
@callback(
    Output('s-output', 'children'),
    Input('s-slider', 'value')
)

@callback(
    Output('P(L|Y)-output', 'children'),
    Input('P(L|Y)-slider', 'value')
)


@callback(
    Output('P(Y)-output', 'children'),
    Input('P(Y)-slider', 'value')
)

@callback(
    Output('P(-L|-Y)-output', 'children'),
    Input('P(-L|-Y)-slider', 'value')
)

def update_s_output(value):
    return f'Selected value of s: {value}'

def update_P_L_Y_output(value):
    return f'Selected value of P(L|Y): {value}'

def update_P_Y_output(value):
    return f'Selected value of P(Y): {value}'

def update_P_notL_notY_output(value):
    return f'Selected value of P(-L|-Y): {value}'

def calculate_new_bar_height():
    return


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
