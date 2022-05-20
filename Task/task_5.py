import pandas as pd 

def run() :
    data = pd.read_csv('./spotify_data.csv', skiprows=0)        # Reading our DataSheet with all the data into a dataframe.
    data = data.loc[:, data.columns.intersection(['artist'])]   # Dropping every colum except the artist colum.
    data = pd.get_dummies(data,columns=['artist']).sum()        # Using get dummies to get the number of how many top songs said artist has produced.
    print(data.sort_values(ascending=False).head(10))           # Sorting our dataframe and taking only top 10 artists.