import numpy as np
import pandas as pd
from helper import str_time_to_num_time, num_time_to_str_time

df = pd.read_csv('../data/vdot-times-jack-daniels-running-formula-2.csv')
data=[]
distances = df.columns[1:]
distances_km = {'1500':1.5, 'Mile':1.60934, '3k':3, '2-mile':3.21869,
                '5k':5, '8k':8, '5-mile':8.04672, '10k':10, '15k':15,
                '10-mile':16.0934, '20k':20, '1/2 Marathon':21.0975, '25k':25,
                 '30k':30, 'Marathon':42.195}
for index, row in df.iterrows():
    vdot = row['VDOT']
    for dist in distances:
        distance = distances_km[dist]
        time = str_time_to_num_time(row[dist])
        data.append([vdot, distance, time])

pd.DataFrame(data, columns=['VDOT', 'Distance', 'Time']).to_csv('../data/vdot-times-jack-daniels-running-formula-2-modified.csv', index=False)