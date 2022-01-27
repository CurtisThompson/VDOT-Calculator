from helper import load_times, str_time_to_num_time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('../data/vdot-times-jack-daniels-running-formula-2-modified.csv')

params = []

# Get powers
data = df.copy()
data['t1'] = data['Time']
data['t2'] = data['t1'] * data['t1']
data['t3'] = data['t2'] * data['t1']
data['t4'] = data['t3'] * data['t1']
data['d1'] = data['Distance']
data['d2'] = data['d1'] * data['d1']
data['d3'] = data['d2'] * data['d1']
data['d4'] = data['d3'] * data['d1']

# Fit model
model = LinearRegression().fit(data[['t1', 't2', 't3', 't4', 'd1', 'd2', 'd3', 'd4']], data['VDOT'])

# Store model parameters
params.append([model.intercept_, model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3], model.coef_[4], model.coef_[5], model.coef_[6], model.coef_[7]])

# Print score
print(model.score(data[['t1', 't2', 't3', 't4', 'd1', 'd2', 'd3', 'd4']], data['VDOT']))

# Store all parameters to csv
coefs = pd.DataFrame(params, columns=['Intercept', 'Coef1', 'Coef2', 'Coef3', 'Coef4', 'Coef5', 'Coef6', 'Coef7', 'Coef8'])
coefs.to_csv('../data/time-distance-to-vdot-coefficients.csv', index=False)