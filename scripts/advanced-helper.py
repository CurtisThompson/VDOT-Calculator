import numpy as np
import pandas as pd

from helper import str_time_to_num_time, num_time_to_str_time


# csv files for converting from different measurements
TIME_TO_VDOT = pd.read_csv('../data/time-to-vdot-coefficients.csv')
VDOT_TO_TIME = pd.read_csv('../data/vdot-to-time-coefficients.csv')
VDOT_TO_PACE = pd.read_csv('../data/vdot-to-pace-coefficients.csv')

# Lists of distances and paces used in calculations
ALL_DISTANCES = ['1500', 'Mile', '3k', '2-mile', '5k', '8k', '5-mile',
                 '10k', '15k', '10-mile', '20k', '1/2 Marathon', '25k',
                 '30k', 'Marathon']
ALL_PACES = ['EL', 'M', 'T', 'I', 'R']

def convert_time_to_vdot(time, distance):
    """Given a specific time over a specific distance, returns VDOT score."""
    # Get equation parameters
    c = TIME_TO_VDOT[TIME_TO_VDOT.Distance==distance].iloc[0].Intercept
    m1 = TIME_TO_VDOT[TIME_TO_VDOT.Distance==distance].iloc[0].Coef1
    m2 = TIME_TO_VDOT[TIME_TO_VDOT.Distance==distance].iloc[0].Coef2
    m3 = TIME_TO_VDOT[TIME_TO_VDOT.Distance==distance].iloc[0].Coef3
    m4 = TIME_TO_VDOT[TIME_TO_VDOT.Distance==distance].iloc[0].Coef4
    
    # If time is string, convert to seconds
    if type(time) is str:
        time = str_time_to_num_time(time)
    
    return c + (m1*time) + (m2*(time**2)) + (m3*(time**3)) + (m4*(time**4))


def convert_vdot_to_time(vdot, distance):
    """Given a VDOT score, returns an approx time for a given distance."""
    # Get equation parameters
    c = VDOT_TO_TIME[VDOT_TO_TIME.Distance==distance].iloc[0].Intercept
    m1 = VDOT_TO_TIME[VDOT_TO_TIME.Distance==distance].iloc[0].Coef1
    m2 = VDOT_TO_TIME[VDOT_TO_TIME.Distance==distance].iloc[0].Coef2
    m3 = VDOT_TO_TIME[VDOT_TO_TIME.Distance==distance].iloc[0].Coef3
    m4 = VDOT_TO_TIME[VDOT_TO_TIME.Distance==distance].iloc[0].Coef4
    
    return c + (m1*vdot) + (m2*(vdot**2)) + (m3*(vdot**3)) + (m4*(vdot**4))


def convert_vdot_to_pace(vdot, pace):
    """Given a VDOT score, returns a training pace."""
    # Get equation parameters
    c = VDOT_TO_PACE[VDOT_TO_PACE.Pace==pace].iloc[0].Intercept
    m1 = VDOT_TO_PACE[VDOT_TO_PACE.Pace==pace].iloc[0].Coef1
    m2 = VDOT_TO_PACE[VDOT_TO_PACE.Pace==pace].iloc[0].Coef2
    m3 = VDOT_TO_PACE[VDOT_TO_PACE.Pace==pace].iloc[0].Coef3
    m4 = VDOT_TO_PACE[VDOT_TO_PACE.Pace==pace].iloc[0].Coef4
    
    return c + (m1*vdot) + (m2*(vdot**2)) + (m3*(vdot**3)) + (m4*(vdot**4))


def equivalent_times(time, distance):
    """Finds equivalent times of different distances for a given race result."""
    # Get equivalent VDOT score
    vdot = convert_time_to_vdot(time, distance)
    
    # From VDOT score, find similar times
    equivs = {}
    for dist in ALL_DISTANCES:
        equivs[dist] = num_time_to_str_time(convert_vdot_to_time(vdot, dist), dp=0)
    equivs[distance] = time
    
    return equivs


def equivalent_paces(time, distance):
    """Finds all training paces for a given race result."""
    # Get equivalent VDOT score
    vdot = convert_time_to_vdot(time, distance)
    
    # From VDOT score, find paces
    equivs = {}
    for pace in ALL_PACES:
        equivs[pace] = num_time_to_str_time(convert_vdot_to_pace(vdot, pace), dp=0)
    
    return equivs


#res = equivalent_times('4:20:00', 'Marathon')
#for key in res:
#    print(key, res[key])

#print()

#res = equivalent_paces('3:30:00', 'Marathon')
#for key in res:
#    print(key, res[key])