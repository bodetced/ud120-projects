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
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

t0 = time()

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

#for c in (10,100,1000,10000,):
for c in (10000,):
    print c
    clf = SVC(kernel="rbf", C=c)
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    pred=clf.predict(features_test)
    acc=accuracy_score(labels_test, pred)

    print "total time:", round(time()-t0, 3), "s"

    print "C:", c, " Accuracy:", acc

    print "10", pred[10]
    print "26", pred[26]
    print "50", pred[50]

    total = 0
    for val in pred:
        if val == 1:
            total += 1

    print "Chris emails:", total
#########################################################