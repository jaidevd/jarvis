#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 DataCultureAnalytics Company
#

"""
Wrappers around sklearn's common cross validation methods.
"""

from sklearn.cross_validation import StratifiedKFold


def report_stratifiedKFold_cv(estimator, X, y, n_folds, metric=None):
    """
    Given an estimator and a training dataset, report the performance on a
    StratifiedKFold cross validation.
    """

    scores = []
    print "Estimator: %s" % str(estimator)
    for train_inds, test_inds in StratifiedKFold(y, n_folds=n_folds):
        xTrain, yTrain = X[train_inds, :], y[train_inds]
        xTest, yTest = X[test_inds, :], y[test_inds]
        estimator.fit(xTrain, yTrain)
        if metric is None:
            score = estimator.score(xTest, yTest)
        else:
            pred = estimator.predict(xTest)
            score = metric(yTest, pred)
            scores.append(score)
        print "\t", score
        scores.append((score, (test_inds, train_inds)))
    return scores
