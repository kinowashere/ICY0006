import numpy as np


def preprocess_data(df):
    print("Preprocessing data...")

    # Drop Categorical / Extra columns
    drop_columns = ['Country or region', 'Overall rank']
    df = df.drop(columns=drop_columns)

    # Fill empty values
    df = df.replace(0, np.NaN)
    df = df.fillna(df.mean())

    return df
