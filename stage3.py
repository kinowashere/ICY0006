#!/usr/bin/env python3

import pandas as pd
import common.describe_data as dd
import common.data_management as dm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.svm import SVR


# Regression without Train / Test data
def show_linear_regression(df, x, y):
    print('Saving Linear Regression: ' + x + ' vs ' + y)
    x_col = df[[x]]
    y_col = df[[y]]
    regressor = LinearRegression()
    regressor.fit(x_col, y_col)
    y_pred = regressor.predict(x_col)
    plt.scatter(x_col, y_col, color='red')
    plt.plot(x_col, y_pred, color='blue')
    plt.title(x + ' vs ' + y)
    plt.xlabel(x)
    plt.ylabel(y)
    x_parsed = dd.parse_to_filename(x)
    y_parsed = dd.parse_to_filename(y)
    plt.savefig('results/linear_regression_' + x_parsed + '_vs_' + y_parsed + '.png')
    plt.close()


def show_polynomial_regression(df, x, y):
    print('Saving Polynomial Regression: ' + x + ' vs ' + y)
    df.sort_values(by=[x], inplace=True)
    svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,
                   coef0=1)
    x_col = df[[x]]
    y_col = df[[y]].values.ravel()
    clf = svr_poly.fit(x_col, y_col)
    y_pred = clf.predict(x_col)
    plt.scatter(x_col, y_col, color='darkorange', label='data')
    plt.plot(x_col, y_pred, color='navy', label='Polynomial Regression')
    plt.title(x + ' vs ' + y)
    plt.xlabel(x)
    plt.ylabel(y)
    x_parsed = dd.parse_to_filename(x)
    y_parsed = dd.parse_to_filename(y)
    plt.savefig('results/polynomial_regression_' + x_parsed + '_vs_' + y_parsed + '.png')
    plt.close()


if __name__ == '__main__':
    whr_df = pd.read_csv('data/data.csv')
    whr_df = dm.preprocess_data(whr_df)
    dd.create_correlation_matrix(whr_df)
    columns = ['GDP per capita', 'Healthy life expectancy', 'Social support']
    for c in columns:
        show_linear_regression(whr_df, c, 'Score')
        show_polynomial_regression(whr_df, c, 'Score')
