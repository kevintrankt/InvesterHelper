import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


# INTERPOLATION
dates = []
prices = []
predictedprices = []
predicteddates = []



def get_data(filename):
    print filename
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)

        # for row in csvFileReader:
        #     if int(row[0].split('-')[0]) > 28:
        #         break
        #     dates.append(int(row[0].split('-')[0]))
        #     prices.append(float(row[1]))
        num = 10
        for row in csvFileReader:
            dates.append(num)
            prices.append(float(row[1]))
            num=num-1
            if num == 0:
                break

    return


def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates),1))

    svr_lin = SVR(kernel= 'rbf',C=1e3,gamma=.1)

    svr_lin.fit(dates,prices)

    plt.scatter(dates,prices, color = 'black', label = 'Data')
    plt.plot(dates,svr_lin.predict(dates),color = 'green', label = 'Linear Model')

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



predict_prices(dates,prices,11)

