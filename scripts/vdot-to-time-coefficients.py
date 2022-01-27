from helper import load_times, str_time_to_num_time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
df = load_times()
for col in df.columns[1:]:
    df[col] = df[col].apply(lambda x: str_time_to_num_time(x))

# Create VDOT powers
df['VDOT1'] = df['VDOT']
df['VDOT2'] = df['VDOT1'] * df['VDOT1']
df['VDOT3'] = df['VDOT2'] * df['VDOT1']
df['VDOT4'] = df['VDOT3'] * df['VDOT1']

params = []

for col in [c for c in df.columns if 'VDOT' not in c]:
    # Fit model
    model = LinearRegression().fit(df[['VDOT1', 'VDOT2', 'VDOT3', 'VDOT4']], df[col])
    
    # Store model parameters
    params.append([col, model.intercept_, model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3]])
    
    # Print score
    print(col, model.score(df[['VDOT1', 'VDOT2', 'VDOT3', 'VDOT4']], df[col]))

# Store all parameters to csv
coefs = pd.DataFrame(params, columns=['Distance', 'Intercept', 'Coef1', 'Coef2', 'Coef3', 'Coef4'])
coefs.to_csv('../data/vdot-to-time-coefficients.csv', index=False)