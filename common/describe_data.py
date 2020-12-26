"""Based on https://machinelearningmastery.com/machine-learning-in-python-step-by-step/"""
import math
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import iqr


def parse_to_filename(var):
    parsed_col = var.replace(" ", "_")
    parsed_col = parsed_col.lower()
    return parsed_col


def print_overview(data_frame, file=''):
    if file:
        print('Saving data frame overview to file', file)
        # If file name is provided redirect sdtout temporarily to file
        prev_stdout = sys.stdout
        sys.stdout = open(file, 'w')

    # Set output options to not omit any columns and limit print width
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)

    print('## Data frame info:')
    print(data_frame.info())
    print('\n')

    print('## Data frame shape:')
    print(str(data_frame.shape[0]) + ' rows')
    print(str(data_frame.shape[1]) + ' columns')
    print('\n')

    print_columns(data_frame)

    print('## Data head and tail:')
    print(data_frame.head(10))
    print('...')
    print(data_frame.tail(5))
    print('\n')

    print('## Numeric values statistics:')
    # Note that float format is set
    pd.set_option('float_format', '{:f}'.format)
    print(data_frame.describe(include='all'))
    print('\n')

    # Restore previous stdout
    if file:
        sys.stdout.close()
        sys.stdout = prev_stdout


def print_columns(data_frame):
    print('## Data frame columns:')
    for column in data_frame.columns:
        print(column)
    print('\n')


def print_categorical(data_frame, columns=[], file=''):
    """Prints out all values and values counts in columns where type is object (categorical data)
    columns names array can be provided as an argument. When not provided, data frame columns is default."""
    if file:
        print('Saving data frame categorical columns values and counts to file', file)
        # If file name is provided redirect sdtout temporarily to file
        prev_stdout = sys.stdout
        sys.stdout = open(file, 'w')

    print('Non-numeric(categorical) columns values and counts:')

    if columns == []:
        columns = data_frame.columns

    for column in columns:
        # Naive solution assuming that all categorical are objects and there
        # are categories at all
        try:
            if data_frame.dtypes[column] == object:
                print(data_frame.groupby(column).size().to_string(), '\n')
        except KeyError:
            print('ERROR: Column', column, 'not found in data frame')

    # Restore previous stdout
    if file:
        sys.stdout.close()
        sys.stdout = prev_stdout


def print_nan_counts(data_frame):
    for column in data_frame.columns:
        nan_sum = data_frame[column].isna().sum()
        if nan_sum > 0:
            print(column, 'nan values sum: ', nan_sum)


def create_correlation_matrix(df):
    print("Creating Correlation Matrix")
    correlation_matrix = df.corr().round(2)
    plt.figure(figsize=(20, 20))
    sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5)
    plt.savefig('results/correlation_matrix.png')
    plt.close()


def f_describe_data(df):
    print("Writing data description...")
    print_overview(
        df, file='results/data_overview.txt'
    )
    print_categorical(
        df, file='results/data_categorical.txt'
    )


def show_distribution_histogram(df, col):
    sns.displot(df[col])
    parsed_col = parse_to_filename(col)
    plt.savefig('results/' + parsed_col + '_distribution_histogram.png')
    plt.close()


def show_tendency_measures(df, columns):
    printout = ""
    printout += "\n\nArithmetic Mean\n-------------------------------------"
    for c in columns:
        printout += "\n" + c + ": " + df.mean()[c].astype('str')
    printout += "\n\nMode\n-------------------------------------"
    for c in columns:
        printout += "\n" + str(df.mode()[c].astype('str'))
        printout += "\n"
    printout += "\nMedian\n-------------------------------------"
    for c in columns:
        printout += "\n" + c + ": " + df.median()[c].astype('str')

    print(printout)

    f = open("results/tendency_measures.txt", "w")
    f.write(printout)
    f.close()


def show_variability_measures(df, columns):
    printout = ""
    printout += "Range\n----------------------------------"
    for c in columns:
        val = df.max()[c] - df.min()[c]
        printout += "\n" + c + ": " + str(val.astype('str'))

    printout += "\n\nInterquartile Range\n----------------------------------"
    for c in columns:
        printout += "\n" + c + ": " + str(iqr(df[c]).astype('str'))

    printout += "\n\nVariance\n----------------------------------"
    for c in columns:
        printout += "\n" + c + ": " + str(df[c].var().astype('str'))

    printout += "\n\nStandard Deviation\n----------------------------------"
    for c in columns:
        sd = math.sqrt(df[c].var())
        printout += "\n" + c + ": " + str(sd)

    print(printout)

    f = open("results/variability_measures.txt", "w")
    f.write(printout)
    f.close()
