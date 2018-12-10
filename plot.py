import plotly
import plotly.tools as tls
import plotly.figure_factory as ff
import plotly.graph_objs as go

import time

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import numpy as np

def distribution(values, algo):
    
    trace1 = go.Histogram(
        x=values,
        opacity=0.75
    )
    #trace2 = go.Histogram(
    #    x=x1,
    #    opacity=0.75
    #)
    data = [trace1]
    layout = go.Layout(barmode='overlay')
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename=algo+str(time.time())+'.html')


def distribution2(values, algo):
    plt.title("Gaussian Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    hist_data = [values]
    group_labels = ['']
    fig = ff.create_distplot(hist_data, group_labels)
    plotly.offline.plot(fig, filename=algo+str(time.time())+'.html')


