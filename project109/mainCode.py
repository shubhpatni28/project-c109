import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("data.csv")

df1 = df["writingScore"].tolist()
print(df1)

mode = statistics.mode(df1)
print("mode : ", mode)

median = statistics.median(df1)
print("median : ", median)

mean = statistics.mean(df1)
print("mean :", mean)

stddev = statistics.stdev(df1)
print("standard deviation : ", stddev) 

first_std = mean-stddev
first_std_end = mean + stddev

sc_std = mean-(2*stddev)
sc_std_end = mean + (2*stddev)

th_std = mean-(3*stddev)
th_std_end = mean + (3*stddev)

data_first_std = [result for result in df1 if result > first_std and result < first_std_end]
data_second_std = [result for result in df1 if result > sc_std and result < sc_std_end]
data_third_std = [result for result in df1 if result > th_std and result < th_std_end]

first_std_per = len(data_first_std) *100.0 / len(df1)
print("first :", first_std_per)

second_std_per = len(data_second_std) *100.0 / len(df1)
print("second :", second_std_per)

third_std_per = len(data_third_std) *100.0 / len(df1)
print("third :", third_std_per)

fig = ff.create_distplot([df1],["dice roll 1000"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std,first_std], y = [0,0.2], mode = "lines", name = "stddev-1"))
fig.add_trace(go.Scatter(x = [sc_std,sc_std], y = [0,0.2], mode = "lines", name = "stddev-2"))
fig.add_trace(go.Scatter(x = [th_std,th_std], y = [0,0.2], mode = "lines", name = "stddev-3"))

fig.add_trace(go.Scatter(x = [first_std_end,first_std_end], y = [0,0.2], mode = "lines", name = "stddev-1"))
fig.add_trace(go.Scatter(x = [sc_std_end,sc_std_end], y = [0,0.2], mode = "lines", name = "stddev-2"))
fig.add_trace(go.Scatter(x = [th_std_end,th_std_end], y = [0,0.2], mode = "lines", name = "stddev-3"))
fig.show()