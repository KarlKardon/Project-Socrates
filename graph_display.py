import exercise_graph
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from datetime import datetime

import weight_graph

"""
Name: Collin Cunningham
UTEID: cbc2948
On my honor, Collin Cunningham, this programming assignment is my own work
and I have not provided this code to any other student.
Complete the following:
0. What is your email in case I have issues while trying to install, run, and
use your program.

collincunningham@gmail.com

1. What is the purpose of your program?

The purpose of my program is to perform statistical analysis and visualize my exercise data which includes specific
exercise performance data as well as my body weight data. This was done through parsing and extracting loosely formatted
data that I would log into my notes app throughout my gym sessions. Essentially, this is another way I can quantify my
gym progress which is a very rewarding thing.

2. List the major features of your program:

    My program produces custom-styled graphs using matplotlib that display my calculated 1 rep max of 3 select exercises
as well as my body weight over time including lines of best fit using linear regression. These lines act as an aid to 
see where my progress is trending towards. Furthermore, the program also prints my percent increase from my best and 
worst data points for all of the categories. 

    In addition, I created a script that would parse my raw data into csv files that are ultimately read to make the 
graphs. This script is not ran in this file since it was only needed to run once to produce the csv files. I include it
in the zip since it played major role in the creation of the final product.

3. What 3rd party modules must be installed for the program to work?
(Must be clear and explicit here or we won't be able to test your program.)
If it is required to install 3rd party modules include the EXACT pip command.



4. List the things your learned while doing this program. Python features,
techniques, third party modules, etc.
5. What was the most difficult thing you had to overcome or learn
to get this program to work?
6. What features would you add next?
"""""


class DataModel:
    def __init__(self, graph, category_name):
        # Will work for both weight and exercise graphs
        self.xpoints_numerical, self.ypoints = graph()
        self.model = []
        self.category_name = category_name
        self.slope, self.intercept, self.r, _, _ = stats.linregress(self.xpoints_numerical, self.ypoints)
        for xpoint in self.xpoints_numerical:
            line_point = self.slope * xpoint + self.intercept
            self.model.append(line_point)

    def get_model(self):
        return self.model

    def get_r(self):
        return self.r

    def get_intercept(self):
        return self.intercept

    def get_slope(self):
        return self.slope

    def print_results(self):
        first_day = min(self.xpoints_numerical)
        last_day = max(self.xpoints_numerical)
        worst_weight = min(self.ypoints)
        best_weight = max(self.ypoints)
        percent_increase = ((best_weight - worst_weight) / worst_weight) * 100.0
        days = last_day - first_day
        print(f"{self.category_name} percent increase: {percent_increase:.2f}% over {days} days")


def setup_graph(filename, plot_num, color_name, category_name):
    if "weight" in filename:
        data_graph = weight_graph.WeightGraph(filename)
    else:
        data_graph = exercise_graph.ExerciseGraph(filename)

    # build model and print results
    x_numerical, bench_y = data_graph()
    model = DataModel(data_graph, category_name)
    model.print_results()

    # Plotting
    plt.subplot(2, 2, plot_num)
    plt.scatter(x_numerical, bench_y, color=color_name)
    plt.plot(x_numerical, model.get_model(), color=color_name)
    plt.grid(color=color_name)

    # Need further date formatting for brevity on graph
    date_format = dates.DateFormatter('%m/%d')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.gca().tick_params(axis='x', colors=color_name)
    plt.gca().tick_params(axis='y', colors=color_name)


def main():
    # styling colors
    color_name = 'papayawhip'
    plt.style.use('dark_background')
    plt.rc('lines', linewidth=2, color=color_name)
    # Ensures grid lines are under graph elements, not over
    plt.rc('axes', axisbelow=True)
    # Size window so it can fit all graphs
    fig = plt.figure(figsize=(12, 10))
    fig.set_facecolor('#161716')
    # font for plot titles
    font1 = {'family': 'serif', 'color': color_name, 'size': 18}
    # font for axis labels
    font2 = {'family': 'serif', 'color': color_name, 'size': 10}
    # padding for plots
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    # Bench Graph
    setup_graph('bench_data.csv', 1, color_name, 'Bench')
    plt.xlabel('Date', fontdict=font2, color=color_name)
    plt.ylabel('Estimated 1 Rep Max (lbs)', fontdict=font2, color=color_name)
    plt.title("Bench Press Progression", fontdict=font1)

    # Hammer Curl Graph
    setup_graph('curl_data.csv', 2, color_name, 'Hammer Curl')
    plt.xlabel('Date', fontdict=font2, color=color_name)
    plt.ylabel('Estimated 1 Rep Max (lbs)', fontdict=font2, color=color_name)
    plt.title('Hammer Curl Progression', fontdict=font1)

    # Lat pull-down Graph
    setup_graph('pulldown_data.csv', 3, color_name, 'Lat Pull-Down')
    plt.xlabel('Date', fontdict=font2, color=color_name)
    plt.ylabel('Estimated 1 Rep Max (lbs)', fontdict=font2, color=color_name)
    plt.title('Lat Pull-Down Progression', fontdict=font1)

    # Weigh-in Graph
    setup_graph('weight_data.csv', 4, color_name, 'Body Weight')
    plt.xlabel('Date', fontdict=font2, color=color_name)
    plt.ylabel('Body Weight (lbs)', fontdict=font2, color=color_name)
    plt.title('Body Weight Progression', fontdict=font1)

    plt.suptitle('Weightlifting and Body Weight Progression', fontdict=font1, fontweight='bold')

    plt.show()


if __name__ == '__main__':
    main()
