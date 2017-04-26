#Sample file to test sklearn

# Plots data
import matplotlib.pyplot as plt

# Contains sample data sets
from sklearn import datasets

# Support vector machine, form of machine learning. Categorizes the numbers
from sklearn import svm

#Loads a lot of data
#Has to convert everything into numbers to normalize data then put onto a scale
digits = datasets.load_digits()

#Sets up classifier (Can be found on SKlearn)
#Gamma ~ gradient deescent of learning rate
clf = svm.SVC(gamma=0.0001, C=100)

#Data to the last number, storing all of the answers
x,y = digits.data[:-10], digits.target[:-10]

clf.fit(x,y)
print (clf.predict(digits.data[-2].reshape(1,-1)))

plt.imshow(digits.images[-2], cmap = plt.get_cmap('gray'), interpolation ="nearest")
plt.show()


