#!/usr/bin/env python3

import pandas as pd
import common.describe_data as dd
import common.data_management as dm


if __name__ == '__main__':
    whr_df = pd.read_csv('data/data.csv')
    dd.f_describe_data(whr_df)
    whr_df = dm.preprocess_data(whr_df)
    dd.create_correlation_matrix(whr_df)
    dd.show_distribution_histogram(whr_df, 'Score')
    dd.show_distribution_histogram(whr_df, 'GDP per capita')
    dd.show_distribution_histogram(whr_df, 'Social support')
    dd.show_distribution_histogram(whr_df, 'Healthy life expectancy')
