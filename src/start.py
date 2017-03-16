import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []


def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)

        for row in csvFileReader:
            if int(row[0].split('-')[0]) > 28:
                break
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))

    return


def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates),1))

    svr_lin = SVR(kernel= 'rbf',C=1e3,gamma=0.1)

    svr_lin.fit(dates,prices)

    plt.scatter(dates,prices, color = 'black', label = 'Data')
    plt.plot(dates,svr_lin.predict(dates),color = 'red', label = 'Linear Model')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Test')

    plt.legend()
    plt.show()

    return svr_lin.predict(x)[0]

get_data('wdc.csv')

print predict_prices(dates,prices,1)

