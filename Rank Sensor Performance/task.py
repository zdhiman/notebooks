# calculates the accuracy of every sensor and arranging them in a descending order

from numpy import genfromtxt
import numpy as np
from sklearn import svm
import operator

## Defining the list to append our training data and test data along with their labels
train_data = []
train_label = []
test_data = []
test_label = []
## Dictionary containing all the results for the Sensors
acc = {}

## Here task_data.csv which contained the sensor data with the labels was read and randomly shuffled so that
## it could be used perfectly for training and testing and hence it was saved into data.csv file


## Reading the data into a numpy array
my_data = genfromtxt('data.csv', delimiter=',')

## Now let us decide that out of 100% data we want our training data to be 80% and 20% will be out test data for each sensor
split = 0.8 * np.shape(my_data)[0]

## The training data is split into 80% of the total data for all the 10 sensors into train_data
## The labels are the first column of the data and splitted same according to the train_data
train_data = my_data[0:int(split), 1:]
train_label = my_data[0:int(split), 0:1]

## Test data and test labels will be the 20% of the my_data
test_data = my_data[int(split):np.shape(my_data)[0], 1:]
test_label = my_data[int(split):np.shape(my_data)[0], 0:1]

## Training on all the sensors data and tesing at the same time
for x in range(1, np.shape(train_data)[1]):

    ## Reading train data starting from 1st sensor --> 10th sensor
    t_data = train_data[:, x]
    ## Reshaping into rank2 numpy array
    t_data = np.reshape(t_data, (np.shape(train_data)[0], 1))
    ## Reading labels starting from 1st sensor --> 10th sensor
    t_label = train_label
    ## Reading test data starting from 1st sensor --> 10th sensor
    te_data = test_data[:, x]
    ## Reshaping into rank2 numpy array
    te_data = np.reshape(te_data, (np.shape(test_data)[0], 1))
    ## Reading labels starting from 1st sensor --> 10th sensor
    te_label = test_label

    ## Considering SVM classifier to provide us with non-linear functionality or hypothesis on the train data
    ## which can be later be used to test our data on it and predict the labels and then compare with the ground truth
    ## to find the accuracy

    ## Here i am considering the gaussian kernel for the SVM
    clf = svm.SVC(kernel='rbf')
    ## Training with the training data and labels
    clf.fit(t_data, t_label)
    ## Predicting the labels of test data and hence calculating the accuracy
    ## Appending to the dictionary accoring to the Sensor values so that later we could arrange them in order
    acc.setdefault('Sensor' + str(x), []).append(clf.score(te_data, te_label))


## Scheming through the values of the keys in the dict to sort them in the descending order and printing them
for key, value in sorted(acc.items(),  key=operator.itemgetter(1),reverse=True):
    print("%s: %s" % (key, value))
