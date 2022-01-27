import numpy as np
import pandas as pd
from helper import str_time_to_num_time, num_time_to_str_time
df = pd.read_csv('../data/vdot-paces-jack-daniels-running-formula-2.csv')
df['EL'] = df['E/L Pace km']
df['M'] = ((df['MP mile'].apply(lambda x: str_time_to_num_time(x))) * 1000) / 1600
df['M'] = df['M'].apply(lambda x: num_time_to_str_time(x, dp=0))
df['T'] = df['T Pace 1000'].apply(lambda x: x[1:])
df['I'] = df['I Pace 400'].apply(lambda x: str_time_to_num_time(x)) * 2.5
df['I'] = df['I'].apply(lambda x: num_time_to_str_time(x, dp=0))
df['R'] = df['R Pace 200'].apply(lambda x: str_time_to_num_time(x)) * 5
df['R'] = df['R'].apply(lambda x: num_time_to_str_time(x, dp=0))

df[['VDOT', 'EL', 'M', 'T', 'I', 'R']].to_csv('../data/vdot-paces-jack-daniels-running-formula-2-modified.csv', index=False)