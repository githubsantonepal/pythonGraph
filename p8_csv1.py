#linear algebra
import numpy as np
#data processing, csv file I/O
import pandas as pd
from matplotlib import cm
from plotly import tools
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot, plot
init_notebook_mode(connected=True)
#from subprocess import check_output
#print(check_output(["ls", "file"]).decode("utf8"))
list_tab10,list_paired=[],[]
tab10_255=cm.tab10(list(range(10)), bytes=255)
paired_255=cm.paired(list(range(10)),bytes=255)
for i in range(10):
    list_tab10.append('rgba({},{}.{}.1)'.format(tab10_255[i,0],tab10_255[i,1],tab10_255[i,2]))
    list_paired.append('rgba({},{}.{}.1)'.format(paired_255[i, 0], paired_255[i, 1], paired_255[i, 2]))
#loadint the csv file as pandas dataframe
data=pd.read_csv('file/migration_nz.csv')
data.info()
data[data.Value.isnull()].sample(10)
print(data[data.Value.isnull()].Country.unique()[:])
print('Missing values from {} until {}'.format(data[data.Value.isnull()].Year.min(),data[data.Value.isnull()].Year.max()))

# searching for the first non zero/null entry for Czechia and
# last non zero/null entry for Czechoslovakia:
print("Last measurement for 'Czechoslovakia' : {}".format(data.query("Country == 'Czechoslovakia' and Value > 0.0").Year.max()))
print("First measurement for 'Czechia' : {}".format(data.query("Country == 'Czechia' and Value > 0.0").Year.min()))

# searching for the first non zero/null entry for Czechia :
print("Last measurement for 'USSR' : {}".format(data.query("Country == 'USSR' and Value > 0.0").Year.max()))
print("First measurement for 'Russia' : {}".format(data.query("Country == 'Russia' and Value > 0.0").Year.min()))

#replacing missing values by zeros
data.fillna(0.0, inplace=True)
data.info()
data_ext = data.pivot_table(index=['Country','Year','Measure'], columns=['Citizenship'], values='Value')
data_ext['Non-NZ Citizen'] = data_ext['Total All Citizenships'] - data_ext['New Zealand Citizen']
data_ext.sample(5)

# same selection and DataFrame manipulation as previsouly
nz_citiz_migr = data_ext.query("Country=='All countries'")['New Zealand Citizen'].unstack(level=2)
wo_citiz_migr = data_ext.query("Country=='All countries'")['Non-NZ Citizen'].unstack(level=2)
nz_citiz_migr.reset_index(level='Country', inplace=True)
wo_citiz_migr.reset_index(level='Country', inplace=True)

#making a multiplot with plotly is a little bit tedious (I think) but not that complicated
# First create a subplot object
fig = tools.make_subplots(rows=3, cols=1, print_grid=False)

# append traces one by one
for i in enumerate(['Arrivals','Departures','Net']):
    if i[0]==0:
        showlegend=True
    else :
        showlegend=False
    trace_nz_tmp = go.Scatter(x=nz_citiz_migr.index, y=nz_citiz_migr[i[1]], name='NZ Citizens',
                              line=dict(color=list_tab10[i[0]]),
                              legendgroup='group_nz', showlegend=showlegend)
    trace_wo_tmp = go.Scatter(x=wo_citiz_migr.index, y=wo_citiz_migr[i[1]], name='Non NZ Citizens',
                              line=dict(color=list_tab10[i[0]], dash='dash'),
                              legendgroup='group_wo', showlegend=showlegend)
    fig.append_trace(trace_nz_tmp, i[0]+1, 1)
    fig.append_trace(trace_wo_tmp, i[0]+1, 1)

# define the layout
fig['layout'].update(height=700, title='New Zealand Migrations - Citizenships Arrivals and Departures')
fig['layout']['xaxis1'].update(dtick=1, tickangle=-60)
fig['layout']['xaxis2'].update(dtick=1, tickangle=-60)
fig['layout']['xaxis3'].update(dtick=1, tickangle=-60, title='Year')
fig['layout']['yaxis1'].update(range=[0,1e5], dtick=2e4, title='Arrivals')
fig['layout']['yaxis2'].update(range=[0,1e5], dtick=2e4, title='Departures')
fig['layout']['yaxis3'].update(range=[-4e4,1e5], dtick=2e4, title='Net')

# plot everything
iplot(fig)

#https://www.kaggle.com/pylablanche/looking-at-new-zealand-migrations