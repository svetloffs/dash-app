# %%
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dlda

# %%
data = dlda.data
start_date = dlda.start_date
end_date = dlda.end_date

print(start_date, end_date)
# time_col = dlda.data['date']
########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
beers_ide=['CS', 'SDIPA', 'IP', 'DDIPA']
beers_dict = [{'label' : beer, 'value' : ide} for beer, ide in (zip(beers, beers_ide))]

ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
mytitle_sales = 'Sales data'

tabtitle='Dash app'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x = beers,
    y = abv_values,
    name = label2,
    marker = {'color':color2}
)

beer_data = [bitterness, alcohol]

beer_layout = go.Layout(
    barmode='group',
    title = mytitle)
# sales_layout = go.Layout(
#     barmode='group',
#     title = mytitle)
# sales_layout = {'data': [ {'x': data['date'],'y': data['Sales'],'type': 'line'} ],
#            'layout': go.Layout(xaxis = {"title":"Time"}, yaxis = {"title":"Sales"}) }

beer_fig = go.Figure(data = beer_data, layout = beer_layout)
# salesdata_fig = go.Figure(data = data, layout = sales_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children = [html.H1(myheading), 
                                  html.Div([dcc.Graph(id = 'example-graph',
                                                      figure = {'data': [ {'x': data['date'],'y': data['Sales'],'type': 'line'} ],
                                                                'layout': go.Layout(xaxis = {"title":"Time"}, yaxis = {"title":"Sales"}) }
                                                     )],
                                           style = {"display":"inline-block", "width":"35%"}),
                                  html.Div([dcc.Graph(id='flyingdog',
                                            figure = beer_fig)],
                                           style = {"display":"inline-block", "width":"35%"})],
                      html.A('Code on Github', href=githublink),
                      html.Br(),
                      html.A('Data Source', href=sourceurl),
                                  html.Label('Dropdown'),
                                  dcc.Dropdown( options = beers_dict,
                                               #             {'label': 'New York City', 'value': 'NYC'},
                                               #             {'label': u'Montréal', 'value': 'MTL'},
                                               #             {'label': 'San Francisco', 'value': 'SF'},
                                               # value='MTL'
                                              ),                           
                                  html.Label('Multi-Select Dropdown'),
                                  dcc.Dropdown(options = beers_dict,
                                               value=['MTL', 'SF'],
                                               multi=True),
                                  html.Label('Radio Items'), 
                                  dcc.RadioItems(options = beers_dict, value='MTL'),
                                  html.Label('Checkboxes'),
                                  dcc.Checklist(options = beers_dict,
                                                value = beers_dict),
                                  html.Label('Text Input'),
                                  dcc.Input(value='MTL', type='text'),
                                  html.Label('Slider'),
                                  dcc.Slider(min=0, max=9,
                                             marks = {i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                                             value = 0),
                      style={'columnCount': 2})

def update_output_div(start_date, end_date):
    print(start_date, end_date)
    return {'data': [go.Scatter(x = data[(data['date'] >= start_date) & 
                                       (data['date'] <= end_date)]['date'], 
                                y = data[(data['date'] >= start_date) & (data['date'] <= end_date)]['Sales'])],
            "layout": go.Layout(xaxis = {"title":"Time"}, yaxis = {"title":"Sales"})}


# app.layout = html.Div([
#     dcc.Markdown(children=markdown_text)
# ])

if __name__ == '__main__':
    app.run_server()

# %%
