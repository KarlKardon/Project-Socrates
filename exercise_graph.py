import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates
from scipy import stats
from datetime import datetime


class ExerciseGraph:
    def __init__(self, filename):
        self.filename = filename
        self.dates, self.set1, self.set2, self.set3 = self.unpack_csv()
        self.xpoints = [datetime.strptime(date, '%m/%d/%Y') for date in self.dates]
        self.ypoints = self.calculate_1rm_per_day()

    # allows us to call class as a function to give x and y values
    def __call__(self, *args, **kwargs):
        # converting to numerical value so I can perform lin reg
        xpoints_numerical = []
        for date in self.xpoints:
            xpoints_numerical.append(mdates.date2num(date))

        return xpoints_numerical, self.ypoints

    def unpack_csv(self):
        data = np.genfromtxt(self.filename, delimiter=',', dtype='<U10', skip_header=1, encoding='utf-8', unpack=True)
        return data

    def epley_formula(self, weight_and_reps):
        weight, rep = map(float, weight_and_reps.split('x'))
        return weight * (1 + rep / 30)

    def calculate_1rm_per_day(self):
        # Check that the input lists are of the same length
        assert len(self.set1) == len(self.set2) == len(self.set3), 'All set arrays must be of the same length.'

        daily_1rms = []

        # Iterate through the sets
        for set1_data, set2_data, set3_data in zip(self.set1, self.set2, self.set3):
            # Calculate 1RM for each set
            daily_1rm_total = (self.epley_formula(set1_data) + self.epley_formula(set2_data) +
                               self.epley_formula(set3_data))

            # Get the average 1RM of the day and add to the list
            avg_1rm = (daily_1rm_total / 3.0)
            daily_1rms.append(avg_1rm)

        return daily_1rms
