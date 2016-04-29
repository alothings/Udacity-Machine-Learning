#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

def random_forest_classifier(feature_train, label_train, feature_test, label_test):
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(criterion='entropy', n_estimators=100, min_samples_split=10,
                                 warm_start=True)
    clf.fit(feature_train, label_train)
    pred = clf.predict(feature_test)
    acc = clf.score(feature_test, label_test)
    print 'Score:', acc
    return clf, pred, acc


def adaboost_classifier(feature_train, label_train, feature_test, label_test):
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier
    clf = AdaBoostClassifier(
        DecisionTreeClassifier(
            max_depth=1,
            min_samples_leaf=1
        ),
        n_estimators=100,
        algorithm="SAMME.R"
    )
    clf.fit(feature_train, label_train)
    pred = clf.predict(feature_test)
    acc = clf.score(feature_test, label_test)
    print 'Score:', acc
    return clf, pred, acc


def k_near_neighbor_classifier(feature_train, label_train, feature_test, label_test):
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(
        n_neighbors=8,
        algorithm='auto',
    )
    clf.fit(feature_train, label_train)
    pred = clf.predict(feature_test)
    acc = clf.score(feature_test, label_test)
    print 'Score:', acc
    return clf, pred, acc


# clf, pred, acc = random_forest_classifier(features_train, labels_train, features_test, labels_test)
# clf, pred, acc = adaboost_classifier(features_train, labels_train, features_test, labels_test)
clf, pred, acc = k_near_neighbor_classifier(features_train, labels_train, features_test, labels_test)

# prettyPicture(clf, features_test, labels_test)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

################################################################################
# RESULTS BEATED UDACITY'S BEST:
# Score: 0.944
# USING:
# clf = KNeighborsClassifier(
#         n_neighbors=8,
#         algorithm='auto',
#     )
#
