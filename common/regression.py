import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from math import sqrt
import common.describe_data as dd


def linear_regression(x, y):
    xf = x.columns[0]
    yf = y.columns[0]
    print(f"Performing Linear Regression: {xf} vs {yf}")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
    clf = LinearRegression()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    plt.scatter(x_test, y_test, color='red', label="Test Data")
    plt.scatter(x_train, y_train, color='darkorange', label='Train Data')
    plt.plot(x_test, y_pred, color='navy', label="Linear Regression")
    plt.title(f"{xf} vs {yf}")
    plt.legend()
    filename = dd.parse_to_filename(f"{xf} vs {yf}.png")
    plt.savefig(f"results/linear_regression_{filename}")
    plt.close()
    return x_train, x_test, y_train, y_test, y_pred


def polynomial_regression(x, y):
    xf = x.columns[0]
    yf = y.columns[0]
    title = f"{xf} vs {yf}"
    print(f"Performing Polynomial Regression: {title}")
    y = y.values.ravel()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
    clf = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1, coef0=1)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    plt.scatter(x_test, y_test, color='red', label="Test Data")
    plt.scatter(x_train, y_train, color='darkorange', label='Train Data')
    plt.scatter(x_test, y_pred, color='navy', label="Linear Regression")
    plt.title(title)
    plt.legend()
    filename = dd.parse_to_filename(f"{title}.png")
    plt.savefig(f"results/polynomial_regression_{filename}")
    plt.close()
    return x_train, x_test, y_train, y_test, y_pred


def test_regression(x, y, y_test, y_pred, regression):
    xf = x.columns[0]
    yf = y.columns[0]
    printout = ""
    title = f"{xf} vs {yf} {regression}\n"
    print(f"Testing {title}...\n")
    printout += title
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    printout += f"RMSE: {rmse}\n"
    mae = mean_absolute_error(y_test, y_pred)
    printout += f"MAE: {mae}\n"
    filename = dd.parse_to_filename(f"{title}.txt")
    f = open(f"results/test_{filename}", "w")
    f.write(printout)
    f.close()
    print(printout)
