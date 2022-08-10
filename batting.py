from ast import increment_lineno
from pybaseball import statcast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#statcast data on all pitches thrown for the months of May and June
data = statcast('2022-05-01', '2022-06-30')
# print(data.shape)

#removing all pitches that didn't result in contact
data2 = data.dropna(subset = ['launch_angle', 'launch_speed', 'estimated_ba_using_speedangle'])
print (data2.head())

#plot of  batted ball's probability of becoming a hit  as a function of its launch angle and exit velocity
fig, ax = plt.subplots(figsize = (8,8))
sns.despine(fig, left = True, bottom = True)
sns.scatterplot(data = data2, x = 'launch_speed', y = 'launch_angle', hue = 'estimated_ba_using_speedangle', palette = 'viridis', ax = ax)
ax.set_title('Hit probability by launch angle and exit velocity');
