from pybaseball import pitching_stats
year = 2022
data = pitching_stats(1870, year)
print(data['ERA'])