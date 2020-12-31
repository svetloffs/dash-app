<<<<<<< HEAD
# %%
=======
>>>>>>> e8bfdcefa1191f4277db265cea125824eb953e17
%config IPCompleter.greedy=True
import pandas as pd
import numpy as np
import datetime
import re
from pandas_datareader import data as web
import plotly.express as px
from datetime import datetime as dt

## data NYSE from: ftp://ftp.nasdaqtrader.com/symboldirectory
df_name = pd.read_csv('~/dash-python-app/datasets/nasdaqlisted.txt', sep = '|', usecols = ['Symbol', 'Security Name'])
df_name['Company'] = df_name['Security Name'].str.split(' ').str[0]
df_name = df_name.drop_duplicates(subset = ['Company']).reset_index()
df_name = df_name.drop(['index'], axis=1)
df_name['Company'] = df_name['Company'].str.strip(',')
## make stock company list
company_dict = []
symbol_dict = []
labl_lst = {}
symb_lst = {}
for company, symbol in zip(df_name['Company'].values, df_name['Symbol'].values):
    company_dict.append({'label' : company, 'value' : symbol})

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

Time_view = 10
end_date = dt.today()
delta = datetime.timedelta(days = 365 * Time_view)
start_date = end_date - delta

rng = pd.date_range(start_date, periods = int(delta.days) // 30, freq = 'm')
# df_stock = pd.DataFrame({'date': rng, 'Sales': np.random.randint(0, 100, len(rng))}) 


app = dash.Dash('Hello World')

chilgren_top = html.Div(className = 'eight columns',
                        children = [html.H2('New York Stock Exange'),
                                    html.H4('build graphics for yuor choise')])

children_right = html.Div(className = 'pretty_container', 
                    children = [html.P('Change view period:', className = 'control_label'),
                                html.Div([dcc.DatePickerRange(id = 'date-picker-range',
                                                              start_date = end_date - datetime.timedelta(days=365),
                                                              end_date = end_date,
                                                              start_date_placeholder_text="Start Period",
                                                              end_date_placeholder_text="End Period",
                                                             ),
                                         ], 
                                         className = 'pretty_container'
                                        ),
                                html.P('Slide left or right:', className = 'control_label'),
                                html.Div(className = 'pretty_container',
                                         children = dcc.Slider(id = 'view-period-slider',
                                                               min = 0,
                                                               max = 10,
                                                               step = 1,
                                                               value = 0)),
                                html.P('Pick company:', className = 'control_label'),
                                html.Div(className = 'div-for-dropdown',
                                         children = [dcc.Dropdown(id = 'my-dropdown',
                                                                  options=company_dict,
#                                                                   value = [df_name['Symbol'].values],
                                                                  value = 'AAPL'
                                                                 ),
                                                    ]
                                        ),
                               ]
                   )
children_left = [html.Div(className = 'pretty_container',
                          children = [html.Div(children =[html.P('Company'), html.H6(id = 'pick-company')], id = 'used-company'),
                                      dcc.Graph(id = 'my-graph')])]

app.layout = html.Div(children = [ html.Div(html.H2('Example dashboard use Python with Dash')), html.Div(className = 'row',
                                            ## top class
                                            children = [html.Div(className = 'four columns div-user-control',
                                                    ## right board view - user control
                                                     children = children_right
                                                                ),
                                                        html.Div(className = 'eight columns div-chart-bk-grey',
                                                    # left board view - graphics view
                                                    children = children_left
                                                   )
                                                       ])
                                 ])
@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value'), Input('date-picker-range', 'start_date')])
def update_graph(selected_dropdown_value, picked_date):
    ### df - Yahoo Stock Exn ##########################
#     print(selected_dropdown_value)
    df_stock = web.DataReader(selected_dropdown_value,
                              'yahoo',
                              picked_date,
                              dt.now()
                             )
#     print(df_stock.head())
    return {'data': [{'x': df_stock.index,
                      'y': df_stock.Close}],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
           }
@app.callback(Output('pick-company', 'children'),
              [Input('my-dropdown', 'value')])
def update_company(selected_dropdown_value):
        company = list(df_name[df_name['Symbol'] == selected_dropdown_value]['Company'])

        return company

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
<<<<<<< HEAD
    app.run_server()
=======
    app.run_server()
>>>>>>> e8bfdcefa1191f4277db265cea125824eb953e17
