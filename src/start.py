import csv
import numpy 
from sklearn.svm import SVR
import matplotlib.pyplot

dates = []
prices = []

def get_data(filename):
    with open(filename,'r') as input:
        csvFileReader = csv.reader(input)
        for row in input:
            dates.append(int(row[0].split('-')[0]))
            