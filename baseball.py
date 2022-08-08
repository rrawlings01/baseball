import pybaseball as pyball
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#retrieves  team records for the NL central for 2022
year = 2022
brewers = pyball.schedule_and_record(year, 'MIL')
cardinals = pyball.schedule_and_record(year, 'STL')
cubs = pyball.schedule_and_record(year, 'CHC')
pirates = pyball.schedule_and_record(year, 'PIT')
reds = pyball.schedule_and_record(year, 'CIN')

#print statesments for record summaries to check whether the data was retrieved correctly
print(brewers.describe())
print(cardinals.describe())
print(cubs.describe())
print(pirates.describe())
print(reds.describe())

#retrive wins, lossess and win percentage to date for each team
brewers['Wins'] = np.where(brewers['W/L']=='W', 1, (np.where(brewers['W/L']=='W-wo', 1, 0))).cumsum()
brewers['Losses'] = np.where(brewers['W/L']=='L', 1, (np.where(brewers['W/L']=='L-wo', 1, 0))).cumsum()
brewers['Win-Percentage'] = brewers['Wins'] / (brewers['Wins'] + brewers['Losses'])

cardinals['Wins'] = np.where(cardinals['W/L']=='W', 1, (np.where(cardinals['W/L']=='W-wo', 1, 0))).cumsum()
cardinals['Losses'] = np.where(cardinals['W/L']=='L', 1, (np.where(cardinals['W/L']=='L-wo', 1, 0))).cumsum()
cardinals['Win-Percentage'] = cardinals['Wins'] / (cardinals['Wins'] + cardinals['Losses'])

cubs['Wins'] = np.where(cubs['W/L']=='W', 1, (np.where(cubs['W/L']=='W-wo', 1, 0))).cumsum()
cubs['Losses'] = np.where(cubs['W/L']=='L', 1, (np.where(cubs['W/L']=='L-wo', 1, 0))).cumsum()
cubs['Win-Percentage'] = cubs['Wins'] / (cubs['Wins'] + cubs['Losses'])

pirates['Wins'] = np.where(pirates['W/L']=='W', 1, (np.where(pirates['W/L']=='W-wo', 1, 0))).cumsum()
pirates['Losses'] = np.where(pirates['W/L']=='L', 1, (np.where(pirates['W/L']=='L-wo', 1, 0))).cumsum()
pirates['Win-Percentage'] = pirates['Wins'] / (pirates['Wins'] + pirates['Losses'])

reds['Wins'] = np.where(reds['W/L']=='W', 1, (np.where(reds['W/L']=='W-wo', 1, 0))).cumsum()
reds['Losses'] = np.where(reds['W/L']=='L', 1, (np.where(reds['W/L']=='L-wo', 1, 0))).cumsum()
reds['Win-Percentage'] = reds['Wins'] / (reds['Wins'] + reds['Losses'])

#Graph win comparisons
plt.rcParams['figure.figsize'] = (8,6)

plt.plot(brewers['Wins'], label = 'Brewers', c = 'navy')
plt.plot(cardinals['Wins'], label = 'Cardinals', c = 'red')
plt.plot(cubs['Wins'], label = 'Cubs', c = 'blue')
plt.plot(pirates['Wins'], label = 'Pirates', c = 'gold')
plt.plot(reds['Wins'], label = 'Reds', c = 'green')

plt.xticks(np.arange(0, len(brewers.index), step=10))
plt.xlabel('Game')
plt.ylabel('Wins')

plt.legend(loc = 'lower right')
plt.title('NL Central Wins Comparison ({})'.format(year))

plt.show()


