#!/usr/bin/env python3

import pandas as pd
import common.describe_data as dd
import common.data_management as dm
import common.regression as reg


if __name__ == '__main__':
    whr_df = pd.read_csv('data/data.csv')
    whr_df = dm.preprocess_data(whr_df)
    dd.create_correlation_matrix(whr_df)
    columns = ['GDP per capita', 'Healthy life expectancy', 'Social support']
    for c in columns:
        reg.show_linear_regression(whr_df, c, 'Score')
        reg.show_polynomial_regression(whr_df, c, 'Score')
