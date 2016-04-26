#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
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
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0,3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1,3), "s"

acc = clf.score(features_test, labels_test)
print acc

#########################################################
"""
    The results when this application was tested 03/14/16 where:
        no. of Chris training emails: 7936
        no. of Sara training emails: 7884
        training time: 1.869 s
        prediction time: 0.259 s
        0.973265073948
"""


