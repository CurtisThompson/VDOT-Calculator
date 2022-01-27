from helper import load_times, str_time_to_num_time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = load_times()

params = []

for col in df.columns[1:]:
    # Get column data as seconds
    data = df[['VDOT', col]].copy()
    data['t1'] = data[col].apply(lambda x: str_time_to_num_time(x))
    
    # Get powers
    data['t2'] = data['t1'] * data['t1']
    data['t3'] = data['t2'] * data['t1']
    data['t4'] = data['t3'] * data['t1']
    
    # Fit model
    model = LinearRegression().fit(data[['t1', 't2', 't3', 't4']], data['VDOT'])
    
    # Store model parameters
    params.append([col, model.intercept_, model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3]])
    
    # Print score
    print(col, model.score(data[['t1', 't2', 't3', 't4']], data['VDOT']))

# Store all parameters to csv
coefs = pd.DataFrame(params, columns=['Distance', 'Intercept', 'Coef1', 'Coef2', 'Coef3', 'Coef4'])
coefs.to_csv('../data/time-to-vdot-coefficients.csv', index=False)