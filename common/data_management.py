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


# Returns y column and dataframe with y column stripped
def get_y(y_column, df):
    print("Getting y and stripping off dataframe...")
    df.sort_values(by=[y_column], inplace=True)
    y = df[[y_column]]
    df = df.drop(labels=y_column, axis=1)
    return df, y

