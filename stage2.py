#!/usr/bin/env python3

import pandas as pd

import common.data_management as dm
import common.describe_data as dd

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    whr_df = pd.read_csv('data/data.csv')
    whr_df = dm.preprocess_data(whr_df)
    columns = ['Score', 'GDP per capita', 'Healthy life expectancy', 'Social support']
    dd.show_tendency_measures(whr_df, columns)
    dd.show_variability_measures(whr_df, columns)
