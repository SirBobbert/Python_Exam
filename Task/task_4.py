import pandas as pd

def run() :
    df = pd.read_csv('spotify_data.csv')                                            # importing dataset
    artist_types = df.drop_duplicates(subset=['artist type']).iloc[:,16].tolist()   # finds all the artist types and makes a list
    for x in artist_types:                                                          # for each element in artist_types
        artist_type = df.loc[df['artist type'] == x]                                # defining what type of artist type we're dealing with
        res = artist_type.groupby(['top genre']).mean()['pop']                      # takes each artist type and finds the average popularity rating based on each genre
        top_3_genre = res.nlargest(3).to_dict()                                     # finds the three most popular genres

        # shows the result
        print('Artist type:', x)
        print('Genres and ratings:', top_3_genre)