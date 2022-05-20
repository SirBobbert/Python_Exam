# imports
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

def run() :
    dataset = pd.read_csv('spotify_data.csv')               # dataset
    means = dataset.groupby('year released').mean()         # finds the average of dataframe based on year released
    #print(means)
    X = means.iloc[:,10].values.reshape(-1, 1)              # preparing values for the regression
    y = means.iloc[:,5].values.reshape(-1, 1)               # x = year, y = val

    regressor = LinearRegression()                          # fitting linear regression to the set
    regressor.fit(X,y)
    y_pred = regressor.predict(X)                           # predicting the set results

    # prints the graph
    plt.scatter(X, y, color = 'red')
    plt.plot(X, regressor.predict(X), color = 'blue')
    plt.title('Val over the years')
    plt.xlabel('Year Released')
    plt.ylabel('Val')
    plt.grid()
    plt.show()

    lm = LinearRegression()
    lm.fit(X, y)
    coefficient = lm.coef_
    print(coefficient)