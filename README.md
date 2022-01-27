# VDOT Calculator
This repository is for calculating a runner's VDOT from one of their long distance running times, as well as calculating other associated values (such as training paces, and predicted times for other distances).

## Usage
There are two main calculators used in this repository.

### HTML Calculator
The first is the HTML calculator, which can be found in `/calculator/calculator.html`. No set-up is required to use this calculator, as it will run in any web browser with Javascript enabled.

To use the HTML calculator, fill in the fields at the top of the page. You will need to enter a recent running result for one of the distances provided (distances are common race distances between 1500m and marathon).

This calculator will then return your VDOT score (see below for more details), your training paces, and equivalent race times for 5k, 10k, half marathon, and marathon.

### Python Methods
Alternatively, you can use the Python methods provided in `/scripts/advanced-helper.py`. To use this file you must have Python 3 installed, along with the [NumPy](https://numpy.org/) and [pandas](https://pandas.pydata.org/) packages.

The main methods you will use within this file are:
 - `convert_time_to_vdot(time, distance)` : to get a VDOT score from a running time
 - `equivalent_times(time, distance)` : to get race times for different distances based on a running time
 - `equivalent_paces(time, distance)` : to get training paces from a running time
 
 See the `/scripts/advanced-helper.py` file for other usable methods.

## Running Information

### VDOT
VDOT refers to the approximate VO2 Max of a runner (approximate is used here as values are based on performance instead of laboratory results). In other words, this is the maximum amount of oxygen the runner can utilise during intense exercise. The more oxygen a runner can use, the more energy that their body can produce. Therefore, we can expect a VDOT score to correlate with performance times.

For more information, see the [Wikipedia entry for VO2 max](https://en.wikipedia.org/wiki/VO2_max).

### Training Paces
Jack Daniels, whose initial research in the 1970s led to widespread use of VDOT among athletes, defined five levels of training intensity that can be calculated from a VDOT score:
 - Easy/Long (EL) Pace: the pace for recovery runs, long runs, warm-ups, and cool downs.
 - Marathon (M) Pace: the pace at which one would expect to complete a marathon.
 - Threshold (T) Pace: the pace aimed to raise the lactate threshold.
 - Interval (I) Pace: the pace aimed to raise the maximum oxygen uptake capacity.
 - Repetition (R) Pace: the pace for 200m-400m interval training.

The conversion from VDOT to paces is based upon your current VDOT, not a hopeful VDOT or a goal time for a future race. Therefore, it is important to use a recently run time when calculating your VDOT and paces, instead of using a time you want to achieve. This will allow you to get the most out of your training without increasing the risk of injury.

## Added Notes
Many of the calculations and data used in this repository is based upon the work of running coach Dr. Jack Daniels. His own VDOT running calculator [can be found online](https://runsmartproject.com/calculator/). Further details can also be found in [his book](https://www.goodreads.com/en/book/show/112152.Daniels_Running_Formula).
