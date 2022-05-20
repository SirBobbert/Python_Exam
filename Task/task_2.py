import matplotlib.pyplot as plt
import pandas as pd

def run() :
    df = pd.read_csv('spotify_data.csv')                        # importing dataset
    genres_with_pop = df.groupby(['top genre']).mean()['pop']   # finds the average pop pr. top genre
    #print(genres_with_pop)
    sorted_df = genres_with_pop.sort_values(ascending=True)     # sorts the dataframe so it will be displayed correctly
    new_dict = sorted_df.to_dict()                              # creates a dict from the dataframe
    plt.rcParams["figure.figsize"] = (35, 10)                   # size of the plot
    plt.bar(new_dict.keys(), new_dict.values())                 # plotting the data

    # eye-candy
    plt.title('Genre popularity over the years')
    plt.xlabel('Genre')
    plt.xticks(rotation=90)
    plt.ylabel('Popularity')

    # prints the plot
    plt.show()