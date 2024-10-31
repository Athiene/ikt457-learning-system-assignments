import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Dash()

# Sample x axis values for the bar chart
SF_x = [1, 2, 3, 4, 5, 6, 7, 8]

# Initial y axis values
SF_y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Helper functions for calculations
def calculate_notLY(value):
    return 1.0-value

def calculate_notY(value):
    return 1.0-value

app.layout = html.Div(
    [
        # Graph to display bar chart
        dcc.Graph(id='bar-chart'),

        # Slider for s
        dcc.Markdown('''#### Slider: s'''),
        dcc.Slider(1.0, 25.0, 0.1, value=12, id="s-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),

        # Slider for P(L|Y)
        dcc.Markdown('''#### Slider: P(L|Y)'''),
        dcc.Slider(0.0, 1.0, 0.01, value=0.5, id="P(L|Y)-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),

        # Slider for P(Y)
        dcc.Markdown('''#### Slider: P(Y)'''),
        dcc.Slider(0.0, 1.0, 0.01, value=0.5, id="P(Y)-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),

        # Slider for P(-L|-Y)
        dcc.Markdown('''#### Slider: P(-L|-Y)'''),
        dcc.Slider(0.0, 1.0, 0.01, value=0.5, id="P(-L|-Y)-slider", marks=None,
                   tooltip={"placement": "bottom", "always_visible": True}),
    ], style={'border': '10px solid #ddd', 'padding': '10px', 'marginTop': '20px', "margin-left": "15%",
              "margin-right": "15%"},
)


# Single callback to use all slider values in one function
@callback(
    Output('bar-chart', 'figure'),
    [
        Input('s-slider', 'value'),
        Input('P(L|Y)-slider', 'value'),
        Input('P(Y)-slider', 'value'),
        
        Input('P(-L|-Y)-slider', 'value')
    ]
)
def update_bar_chart(s, P_LY, P_Y, P_notL_notY):

    big_equation = ((P_LY*P_Y) + (P_notL_notY * calculate_notY(value=P_Y)))
    SF_y[0] = s**0 * (P_Y**4) * P_LY**0 * (calculate_notLY(value=P_LY)**7) * big_equation**0
    SF_y[1] = s**1 * (P_Y**3) * P_LY**0 * (calculate_notLY(value=P_LY)**6) * big_equation**1 
    SF_y[2] = s**2 * (P_Y**2) * P_LY**0 * (calculate_notLY(value=P_LY)**5) * big_equation**2
    SF_y[3] = s**3 * (P_Y**1) * P_LY**0 * (calculate_notLY(value=P_LY)**4) * big_equation**3
    SF_y[4] = s**4 * (P_Y**0) * P_LY**0 * (calculate_notLY(value=P_LY)**3) * big_equation**4
    SF_y[5] = s**5 * (P_Y**0) * P_LY**1 * (calculate_notLY(value=P_LY)**2) * big_equation**4
    SF_y[6] = s**6 * (P_Y**0) * P_LY**2 * (calculate_notLY(value=P_LY)**1) * big_equation**4
    SF_y[7] = s**7 * (P_Y**0) * P_LY**3 * (calculate_notLY(value=P_LY)**0) * big_equation**4


        

    # Normalize SF_y to make the sum equal to 1
    total = sum(SF_y)
    SF_y_normalized = [value / total for value in SF_y]

    # Create the bar chart figure
    fig = go.Figure(data=[
        go.Bar(x=SF_x, y=SF_y_normalized, name='SF'),
    ])

    # Set title, labels, and y axis to range from 0 to 1
    fig.update_layout(
        title="Interactive Stationary Distribution Bar Chart",
        xaxis_title="States",
        yaxis_title="Probability",
        yaxis_range=[0, 1] 
    )

    return fig  


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

