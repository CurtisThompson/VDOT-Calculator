import numpy as np
import pandas as pd


def load_times():
    df = pd.read_csv('../data/vdot-times-jack-daniels-running-formula-2.csv')
    return df


def load_paces():
    df = pd.read_csv('../data/vdot-paces-jack-daniels-running-formula-2.csv')
    return df


def str_time_to_num_time(time):
    if time == '-':
        return -1
    
    time_parts = str(time).split(':')
    
    hours = float(time_parts[-3]) if len(time_parts) > 2 else 0
    mins = float(time_parts[-2]) if len(time_parts) > 1 else 0
    secs = float(time_parts[-1])
    
    return (3600*hours) + (60*mins) + secs


def num_time_to_str_time(time):
    str_time = ''
    
    hours = int(time // 3600)
    if hours > 0:
        str_time += str(hours)
    time -= hours * 3600
    
    mins = int(time // 60)
    if (mins > 0) or (len(str_time) > 0):
        if len(str_time) > 0:
            str_time += ':'
            if mins < 10:
                str_time += '0'
        str_time += str(mins)
    time -= mins * 60
    
    secs = round(time, 2)
    if (secs > 0) or (len(str_time) > 0):
        if len(str_time) > 0:
            str_time += ':'
            if secs < 10:
                str_time += '0'
        str_time += str(secs) if str(secs)[-2:] != '.0' else str(secs)[:-2]
    
    return str_time


def vdot_to_running_times(vdot, data=load_times()):
    times = data[data.VDOT==vdot].copy()
    for col in times[1:]:
        try:
            times[col] = times[col].apply(lambda x: num_time_to_str_time(x))
        except:
            times[col] = times[col]
    return times.iloc[0]


def running_time_to_vdot(time, distance, data=load_times()):
    for col in data.columns[1:]:
        data[col] = data[col].apply(lambda x: str_time_to_num_time(x))
    data = data[['VDOT', distance]]
    
    my_time = str_time_to_num_time(time)
    
    above_time = [x for x in data[distance] if x >= my_time]
    vdot = data[data[distance]==min(above_time)].VDOT.iloc[0]
    return vdot


def time_to_similar_times(time, distance, data=load_times()):
    vdot = running_time_to_vdot(time, distance, data=data)
    return vdot_to_running_times(vdot, data=data)


def time_to_training_paces(time, distance, time_data=load_times(), pace_data=load_paces()):
    vdot = running_time_to_vdot(time, distance, data=time_data)
    return vdot_to_running_times(vdot, data=pace_data)



print(time_to_similar_times('19:00', '5k'))
print()
print(time_to_training_paces('19:00', '5k'))