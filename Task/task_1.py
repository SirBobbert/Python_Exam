import pandas as pd

def task1() :
    data = pd.read_csv('./spotify_data.csv', skiprows=0)                # Reading our DataSheet with all the data into a dataframe.
    genres = ['dance pop', 'modern alternative rock', 'acoustic pop']   # Our 3 chosen genres for this assignment.
    for x in genres : 
        df = data[(data['top genre']==x)]                       # Chosing the genre which we will use for the calculations.
        df = df.sort_values('pop', ascending=False).head(5)     # Sorting the dataframe so that the most popular songs are placed highest, and then takes top 5.
        avg = (df['bpm'].sum()/5)                               # Add the top 5 songs beats per minute togheter and divides that by 5.
        print(x + ' average beats per minute for the top 5 most popular songs = ' + str(avg))