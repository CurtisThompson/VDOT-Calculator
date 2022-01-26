# 5k Times Modelling

Using the `scripts/5k-time-plotting.py` script, we were able to look at how the 5k times are correlated with VDOT scores.

## Plotting 5k Times

If we plot a list of 5k times against known, whole VDOT scores then we can clearly see there is a correlation between the two.

![Correlation plot](/generated-notes/5k-models/regular-plot.png)

With such a simple correlation, it looks likely that we can model it with just a regression model.

## Building Regression Models

### Linear Model

If we first build a linear regression model with 5k times (in seconds) to predict VDOT score, we can see the correlation.

![Linear plot](/generated-notes/5k-models/linear-plot.png)

Our model has an intercept of 116.44... and a coefficient of -0.05186..., giving an `r` score of 0.94074. We can write this as VDOT = 116.44 - (0.05186 * time_5k). This gives us a good approximation, but we can see from both the plot and the score that we can do better.

### Multiple Regression

We will try new models with powers of 2, 3, and 4.

![Multiple plot](/generated-notes/5k-models/multi-plot.png)

Our associated `r` scores are:

| Power  | Score |
| ------------- | ------------- |
| 1  | 0.9407437957743374  |
| 2  | 0.9965389674493701  |
| 3  | 0.9997947879113098  |
| 4  | 0.9999863609763706  |

With this, we can see that our model improves as we add more powers. However, the score for our best model is already sufficiently good, so we can use that.

VDOT = 320.21840994212795 + (-5.85338453e-01 * time_5k) + (4.99386989e-04 * time_5k^2) + (-2.05665011e-07 * time_5k^3) + (3.29250289e-11 * time_5k^4)

This equation can be used to get more specific VDOT scores, instead of whole numbers (or just whole numbers provided in the table). While it be not look evidently useful, it can be used for more fine-tuned automatic pacing recommendations.
