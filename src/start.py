"""This module is used to open csv files containing stock prices (from https://www.google.com/finance)"""
import csv
"""This module is used to reshape data from csv to be plotted properly"""
import numpy as np
"""This module is used to make a simple neural network"""
from sklearn.svm import SVR
"""This module is used to visualize and plot data"""
import matplotlib.pyplot as plt



dates = [] # Array to hold dates [X - February 28]
prices = [] # Array to hold stock open prices
predictedprices = [] # Array to hold prices predicted from RBF 
predicteddates = [] # Array to hold dates following February 28th


"""Opens stock data from finance.google.com csv file. Dates end at Feburary 28th"""
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        num = 100
        for row in csvFileReader:
            dates.append(num)
            prices.append(float(row[1]))
            num = num-1
            if num == 0:
                break

    return

"""Adjust predicted prices based off of 'x', factor of good/bad. -5<x<5, 5 being great press, -5 being bad press"""
def adjust_prices(dates,prices, predicteddates, predictedprices, x):
    return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates),1))

    svr_lin = SVR(kernel= 'rbf',C=1e3,gamma=.1)

    svr_lin.fit(dates,prices)

    predictedprices.append(svr_lin.predict(x)[0])
    predictedprices.append(svr_lin.predict(x+1)[0])
    predictedprices.append(svr_lin.predict(x+2)[0])
    predictedprices.append(svr_lin.predict(x+3)[0])
    predictedprices.append(svr_lin.predict(x+4)[0])
    predictedprices.append(svr_lin.predict(x+5)[0])
    predictedprices.append(svr_lin.predict(x+6)[0])
    predictedprices.append(svr_lin.predict(x+7)[0])

    predicteddates.append(x)
    predicteddates.append(x+1)
    predicteddates.append(x+2)
    predicteddates.append(x+3)
    predicteddates.append(x+4)
    predicteddates.append(x+5)
    predicteddates.append(x+6)
    predicteddates.append(x+7)

    plt.scatter(dates,prices, color = 'black', label = 'Data')
    plt.plot(dates,svr_lin.predict(dates),color = 'green', label = 'Linear Model')



    print 'March 1:',svr_lin.predict(x)[0]
    print 'March 2:',svr_lin.predict(x+1)[0]
    print 'March 3:',svr_lin.predict(x+2)[0]
    print 'March 4:',svr_lin.predict(x+3)[0]
    print 'March 5:',svr_lin.predict(x+4)[0]
    print 'March 6:',svr_lin.predict(x+5)[0]
    print 'March 7:',svr_lin.predict(x+6)[0]
    print 'March 8:',svr_lin.predict(x+7)[0]

    plt.scatter(predicteddates,predictedprices,color = 'green', label = 'Predictions')





    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Test')

    # plt.legend()
    plt.show()

    return svr_lin.predict(x)[0]

# get_data('aapl.csv')
# get_data('wdc.csv')
get_data('gpro.csv')



predict_prices(dates,prices,101)

