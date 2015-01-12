__author__ = 'adomas'

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from eda import *

data = read_data(path)
Y = data.Cover_Type
X = data.drop('Cover_Type', axis=1)
model = LogisticRegression(C=0.01, penalty='l1',tol=0.01)
model.fit(X,Y)