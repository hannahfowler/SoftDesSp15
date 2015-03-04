import matplotlib.pyplot as plt 
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
num_trials = 10
train_percentages = range(5,95,5)
test_accuracies = []

model = LogisticRegression(C=10**-10)

for i in train_percentages:
	X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=i)

model.score(X_test, y_test)
model.fit(X_train, y_train)


fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()