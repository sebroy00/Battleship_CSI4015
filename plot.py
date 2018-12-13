import plotly
import plotly.tools as tls
import plotly.figure_factory as ff
import plotly.graph_objs as go

import time

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import numpy as np

def distribution(data, group_labels, colors):
    hist_data = data
    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, show_hist=False, curve_type='normal', colors=colors)
    fig['layout'].update(title='Battleship Algorithms: Distplot with Normal Distribution')

    plotly.offline.plot(fig, filename='battleship-algos-'+str(time.time())+'.html')


def distribution2(values, algo):
    plt.title("Gaussian Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    hist_data = [values]
    group_labels = ['']
    fig = ff.create_distplot(hist_data, group_labels)
    plotly.offline.plot(fig, filename=algo+str(time.time())+'.html')


