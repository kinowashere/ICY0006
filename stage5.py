#!/usr/bin/env python3
import common.data_management as dm
import common.regression as r
import pandas as pd

if __name__ == '__main__':
    print("Stage 5")
    whr_df = pd.read_csv('data/data.csv')
    whr_df = dm.preprocess_data(whr_df)
    whr_df, y = dm.get_y('Score', whr_df)
    columns = ['GDP per capita', 'Healthy life expectancy', 'Social support']
    for c in columns:
        x = whr_df[[c]]
        x_train, x_test, y_train, y_test, y_pred = r.linear_regression(x, y)
        r.test_regression(x, y, y_test, y_pred, 'Linear')
        x_train, x_test, y_train, y_test, y_pred = r.polynomial_regression(x, y)
        r.test_regression(x, y, y_test, y_pred, 'Polynomial')
