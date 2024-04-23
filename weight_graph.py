import numpy as np
import matplotlib.dates as mdates
from datetime import datetime


#Class oriented towards generating a graph for tracking weigh-in data
class WeightGraph:
    def __init__(self, filename):
        self.filename = filename
        self.dates, self.weights = self.unpack_csv()
        self.xpoints = [datetime.strptime(date, '%m/%d/%Y') for date in self.dates]
        self.ypoints = [float(weight) for weight in self.weights]

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



