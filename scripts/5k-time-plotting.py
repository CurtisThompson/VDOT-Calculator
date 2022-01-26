from helper import load_times, str_time_to_num_time

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Load in 5k times and VDOT scores
df = load_times()
df = df[['VDOT', '5k']]
df['5k Time'] = df['5k'].apply(lambda x: str_time_to_num_time(x))


# Create a plot of 5k times against VDOT
df.plot(y='VDOT',
        x='5k Time',
        kind='scatter',
        grid=True,
        title='5k Times Against VDOT')
plt.xticks(ticks=[900, 1200, 1500, 1800],
           labels=['15:00', '20:00', '25:00', '30:00'])
plt.savefig('../generated-notes/5k-models/regular-plot.png')

####################
# We will create a linear regression model and plot results

# Plot a linear regression
model = LinearRegression().fit(df[['5k Time']], df['VDOT'])
print(model.coef_)
print(model.intercept_)
print(model.score(df[['5k Time']], df['VDOT']))

# Get presumed VDOTs from model
plot_space = np.linspace(700, 1900, num=50)
vdots = model.intercept_ + (plot_space * model.coef_[0])

# Plot true, and model predictions
df.plot(y='VDOT',
        x='5k Time',
        kind='scatter',
        grid=True,
        title='5k Times Against VDOT (with Linear Regression Model)')
plt.xticks(ticks=[900, 1200, 1500, 1800],
           labels=['15:00', '20:00', '25:00', '30:00'])
plt.plot(plot_space, vdots)
plt.savefig('../generated-notes/5k-models/linear-plot.png')

####################
# We will create multiple regression models and plot results

# Create multiple regression models
df['5k_1'] = df['5k Time']
df['5k_2'] = df['5k_1'] * df['5k_1']
df['5k_3'] = df['5k_2'] * df['5k_1']
df['5k_4'] = df['5k_3'] * df['5k_1']
model_1 = LinearRegression().fit(df[['5k_1']], df['VDOT'])
model_2 = LinearRegression().fit(df[['5k_1', '5k_2']], df['VDOT'])
model_3 = LinearRegression().fit(df[['5k_1', '5k_2', '5k_3']], df['VDOT'])
model_4 = LinearRegression().fit(df[['5k_1', '5k_2', '5k_3', '5k_4']], df['VDOT'])

# Get model predictions
plot_space = np.linspace(700, 1900, num=50)
vdots_1 = model_1.intercept_ + (plot_space * model_1.coef_[0])
vdots_2 = model_2.intercept_ + (plot_space * model_2.coef_[0]) + ((plot_space**2)*model_2.coef_[1])
vdots_3 = model_3.intercept_ + (plot_space * model_3.coef_[0]) + ((plot_space**2)*model_3.coef_[1]) + ((plot_space**3)*model_3.coef_[2])
vdots_4 = model_4.intercept_ + (plot_space * model_4.coef_[0]) + ((plot_space**2)*model_4.coef_[1]) + ((plot_space**3)*model_4.coef_[2]) + ((plot_space**4)*model_4.coef_[3])

# Plot true, and model predictions
df.plot(y='VDOT',
        x='5k Time',
        kind='scatter',
        grid=True,
        title='5k Times Against VDOT (with Multiple Regression Models)')
plt.xticks(ticks=[900, 1200, 1500, 1800],
           labels=['15:00', '20:00', '25:00', '30:00'])
plt.plot(plot_space, vdots_1, label='Power 1')
plt.plot(plot_space, vdots_2, label='Power 2')
plt.plot(plot_space, vdots_3, label='Power 3')
plt.plot(plot_space, vdots_4, label='Power 4')
plt.legend()
plt.savefig('../generated-notes/5k-models/multi-plot.png')

# Output scores for each model
print()
print('Model 1:', model_1.score(df[['5k_1']], df['VDOT']))
print('Model 2:', model_2.score(df[['5k_1', '5k_2']], df['VDOT']))
print('Model 3:', model_3.score(df[['5k_1', '5k_2', '5k_3']], df['VDOT']))
print('Model 4:', model_4.score(df[['5k_1', '5k_2', '5k_3', '5k_4']], df['VDOT']))

# Print coefs and intercept for model 4
print()
print('Model 4')
print('Coefs:    ', model_4.coef_)
print('Intercept:', model_4.intercept_)

####################
# These are helper functions created from the power 4 model

def fivek_time_to_vdot(time):
    c = 320.21840994212795
    m = [-5.85338453e-01,4.99386989e-04,-2.05665011e-07,3.29250289e-11]
    
    secs = str_time_to_num_time(time)
    vdot = c + (secs*m[0]) + ((secs**2)*m[1]) + ((secs**3)*m[2]) + ((secs**4)*m[3])
    return vdot

print()
print('20:00 to ', fivek_time_to_vdot('20:00'))
print('22:00 to ', fivek_time_to_vdot('22:00'))
print('24:00 to ', fivek_time_to_vdot('24:00'))
print('26:00 to ', fivek_time_to_vdot('26:00'))