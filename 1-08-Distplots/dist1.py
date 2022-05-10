#######
# This distplot uses plotly's Figure Factory
# module in place of Graph Objects
######
import plotly.offline as pyo
import plotly.figure_factory as ff # does more advanced figures
import numpy as np

x = np.random.randn(1000) # assign x to 1000 random data points
hist_data = [x]
group_labels = ['distplot'] # actual label for x data 

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='basic_distplot.html')
