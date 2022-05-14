"""
5.	Hvilken artist har haft flest populære sange
    a.	Her gør vi brug af get_dummies
    b.	Her vil vi bruge pandas dataframe
"""
import pandas as pd 

data = pd.read_csv('./spotify_data.csv', skiprows=0)
data.drop(['title','top genre','year released','added','bpm','nrgy','dnce','dB', 'live','val','dur','acous','spch','pop','top year','artist type'],'columns',inplace=True)
data = pd.get_dummies(data,columns=['artist'])
data = data.sum()
print(data.sort_values(ascending=False).head(10))

