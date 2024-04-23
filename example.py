import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from datetime import datetime
from scipy import stats

from exercise_graph import ExerciseGraph

"""
Name:
UTEID: cbc2948
On my honor, Collin Cunningham, this programming assignment is my own work
and I have not provided this code to any other student.
Complete the following:
0. What is your email in case I have issues while trying to install, run, and
use your program.

collincunningham@gmail.com

1. What is the purpose of your program?



2. List the major features of your program:
3. What 3rd party modules must be installed for the program to work?
(Must be clear and explicit here or we won't be able to test your program.)
If it is required to install 3rd party modules include the EXACT pip command.
4. List the things your learned while doing this program. Python features,
techniques, third party modules, etc.
5. What was the most difficult thing you had to overcome or learn
to get this program to work?
6. What features would you add next?
"""""


# First need to unpack all csv files
def unpack_csv(filename):
    data = np.genfromtxt(filename, delimiter=',', dtype='<U9', skip_header=1, encoding='utf-8', unpack=True)
    date, set1, set2, set3 = data
    return date, set1, set2, set3


# Function to calculate 1 rep max using the Epley formula
# This way we can boil down weights, reps, and sets down to a single value
def epley_formula(weight_and_reps):
    split_list = weight_and_reps.split('x')
    weight = int(split_list[0])
    rep = int(split_list[1])
    return weight * (1 + rep / 30)


# Extracts list of 1rms from weight and rep count data
def calculate_1rm_per_day(set1, set2, set3):
    # Check that the input lists are of the same length
    assert len(set1) == len(set2) == len(set3), 'All set arrays must be of the same length.'

    daily_1rms = []

    # Iterate through the sets
    for set1_data, set2_data, set3_data in zip(set1, set2, set3):
        # Calculate 1RM for each set
        daily_1rm_total = epley_formula(set1_data) + epley_formula(set2_data) + epley_formula(set3_data)

        # Get the average 1RM of the day and add to the list
        avg_1rm = (daily_1rm_total / 3.0)
        daily_1rms.append(avg_1rm)

    return daily_1rms


bench_date, bench_set1, bench_set2, bench_set3 = unpack_csv("bench_data.csv")

bench_1rms = calculate_1rm_per_day(bench_set1, bench_set2, bench_set3)

# Convert date strings to datetime objects
bench_date = [datetime.strptime(date, "%m/%d/%Y") for date in bench_date]

# Need further date formatting for brevity on graph
date_format = dates.DateFormatter('%m/%d')
plt.gca().xaxis.set_major_formatter(date_format)

xpoints = bench_date
xpoints_numerical = [dates.date2num(date) for date in xpoints]  # converting to numerical value so I can perform lin reg
ypoints = bench_1rms

# Linear regression of data
slope, intercept, r, p, std_err = stats.linregress(xpoints_numerical, ypoints)

data_model = []

# Iterate through x points to find y values for line of best fit
for xpoint in xpoints_numerical:
    line_point = slope * xpoint + intercept
    data_model.append(line_point)

plt.scatter(xpoints, ypoints)
plt.plot(xpoints_numerical, data_model)
plt.show()


plt.xlabel("Date")
plt.ylabel("Estimated 1 Rep Max (lbs)")
font1 = {'family': 'serif', 'color': 'black', 'size': 20}
plt.title("Bench Press Data", fontdict=font1)

print(r)
