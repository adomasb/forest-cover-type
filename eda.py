__author__ = 'adomas'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = '/home/adomas/forest-cover-type/train.csv'
# read data
def read_data(path):
    data = pd.read_csv(path).drop('Id', axis=1)
    return data


# hists
# plt.hist(data.Elevation)
# plt.hist(data.Aspect)
# plt.hist(data.Slope)
# plt.scatter(data.Horizontal_Distance_To_Hydrology, data.Vertical_Distance_To_Hydrology)
# plt.scatter(data.Horizontal_Distance_To_Roadways, data.Horizontal_Distance_To_Fire_Points)