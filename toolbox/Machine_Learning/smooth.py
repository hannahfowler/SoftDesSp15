import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
#print data.DESCR
num_trials = 10
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

# train a model with training percentages between 5 and 90 (see train_percentages) and evaluate
# the resultant accuracy.
# You should repeat each training percentage num_trials times to smooth out variability
# for consistency with the previous example use model = LogisticRegression(C=10**-10) for your learner

# TODO: your code here
model = LogisticRegression(C=10**10)
for j in range(len(train_percentages)):
	average = []
	for i in range(num_trials):
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=train_percentages[j])
		model.fit(X_train, y_train)
		average.append(model.score(X_test, y_test))
	acc = sum(average)/len(average)
	test_accuracies[j] = acc 


fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()