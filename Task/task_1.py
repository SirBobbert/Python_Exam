"""
1.	Hvad er den mest optimale bpm indenfor dance pop, modern alternative rock og acoustic pop
    a.	Vi vil tage top-5 mest populære sange inde for hver genre for at finde den gennemsnitlige bpm for hver genre
    b.	Her vil vi bruge pandas dataframe
"""
import pandas as pd

data = pd.read_csv('./spotify_data.csv', skiprows=0)
#print(data)
dance_pop = data[(data['top genre']=='dance pop')]
dance_pop = dance_pop.sort_values('pop', ascending=False).head(5)
dance_pop_average = (dance_pop['bpm'].sum()/5)
print('dance pop average beats per minute for top 5 most popular songs.')
print(dance_pop_average)

modern_alternative_rock = data[(data['top genre']=='modern alternative rock')]
modern_alternative_rock = modern_alternative_rock.sort_values('pop', ascending=False).head(5)
modern_alternative_rock_average = (modern_alternative_rock['bpm'].sum()/5)
print('modern alternative rock average beats per minute for top 5 most popular songs.')
print(modern_alternative_rock_average)

acoustic_pop = data[(data['top genre']=='acoustic pop')]
acoustic_pop = acoustic_pop.sort_values('pop', ascending=False).head(5)
acoustic_pop_average = (acoustic_pop['bpm'].sum()/5)
print('acoustic pop average beats per minute for top 5 most popular songs.')
print(acoustic_pop_average)