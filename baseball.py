from ast import increment_lineno
import pybaseball as pyball
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

year = 2018
brewers = pyball.schedule_and_record(year, 'MIL')
cardinals = pyball.schedule_and_record(year, 'STL')
cubs = pyball.schedule_and_record(year, 'CHC')
pirates = pyball.schedule_and_record(year, 'PIT')
reds = pyball.schedule_and_record(year, 'CIN')

print(brewers.describe())

