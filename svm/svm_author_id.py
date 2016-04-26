#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### My Code

from sklearn.svm import SVC
clf = SVC(kernel="rbf", C=10000.0)

# REDUCING FEATURES TO 1%
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0,3), "s"

t1 = time()
pred = clf.predict(features_test)
# pred10 = clf.predict(features_test[10])
# pred26 = clf.predict(features_test[26])
# pred50 = clf.predict(features_test[50])
print "Starting Predictions"
# print pred10
# print pred26
# print pred50
print "prediction time:", round(time()-t1,3), "s"
count = 0

# for i in pred:
#     if i == 1:
#         count += 1
# print count

acc = clf.score(features_test, labels_test)
print acc
#########################################################


