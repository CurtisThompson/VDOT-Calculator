import numpy as np
import pandas as pd


def load_times():
    """Load the VDOT to distance times from file."""
    df = pd.read_csv('../data/vdot-times-jack-daniels-running-formula-2.csv')
    return df


def load_paces():
    """Load the VDOT to training paces from file."""
    df = pd.read_csv('../data/vdot-paces-jack-daniels-running-formula-2.csv')
    return df


def str_time_to_num_time(time):
    """Convert a string time (e.g. 1:36:50) to seconds."""
    
    # If time is -, then no time found
    if time == '-':
        return -1
    
    # Split time into hours, minutes, seconds
    time_parts = str(time).split(':')
    
    # Store each time part as a float number
    hours = float(time_parts[-3]) if len(time_parts) > 2 else 0
    mins = float(time_parts[-2]) if len(time_parts) > 1 else 0
    secs = float(time_parts[-1])
    
    # Calculate seconds and return
    return (3600*hours) + (60*mins) + secs


def num_time_to_str_time(time, dp=2):
    """Convert a number of seconds to a string time (e.g. 1:36:50)."""
    str_time = ''
    
    # Get number of whole hours
    hours = int(time // 3600)
    # Add to string time
    if hours > 0:
        str_time += str(hours)
    # Remove hours from time, for minutes calculation
    time -= hours * 3600
    
    # Get number of whole minutes
    mins = int(time // 60)
    # Add to string time
    if (mins > 0) or (len(str_time) > 0):
        if len(str_time) > 0:
            str_time += ':'
            if mins < 10:
                str_time += '0'
        str_time += str(mins)
    # Remove minutes from time, for seconds calculation
    time -= mins * 60
    
    # Get number of seconds to 2 dp (or input dp)
    secs = round(time, dp)
    # Add to string time
    if (secs > 0) or (len(str_time) > 0):
        if len(str_time) > 0:
            str_time += ':'
            if secs < 10:
                str_time += '0'
        str_time += str(secs) if str(secs)[-2:] != '.0' else str(secs)[:-2]
    
    # Return string time
    return str_time


def vdot_to_running_times(vdot, data=load_times()):
    """Get a Series of distance times from VDOT."""
    times = data[data.VDOT==vdot].copy()
    for col in times[1:]:
        try:
            times[col] = times[col].apply(lambda x: num_time_to_str_time(x))
        except:
            times[col] = times[col]
    return times.iloc[0]


def running_time_to_vdot(time, distance, data=load_times()):
    """Convert a distance time to VDOT."""
    
    # Get only the VDOT and distance columns (as seconds)
    for col in data.columns[1:]:
        data[col] = data[col].apply(lambda x: str_time_to_num_time(x))
    data = data[['VDOT', distance]]
    
    # Convert given time to seconds
    my_time = str_time_to_num_time(time)
    
    # Find the best VDOT worse than the given time
    above_time = [x for x in data[distance] if x >= my_time]
    vdot = data[data[distance]==min(above_time)].VDOT.iloc[0]
    return vdot


def time_to_similar_times(time, distance, data=load_times()):
    """Given a time, find equivalent times for other distances."""
    vdot = running_time_to_vdot(time, distance, data=data)
    return vdot_to_running_times(vdot, data=data)


def time_to_training_paces(time, distance, time_data=load_times(), pace_data=load_paces()):
    """Given a time, find the equivalent training paces."""
    vdot = running_time_to_vdot(time, distance, data=time_data)
    return vdot_to_running_times(vdot, data=pace_data)



#print(time_to_similar_times('19:00', '5k'))
#print()
#print(time_to_training_paces('19:00', '5k'))