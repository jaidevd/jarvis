#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 DataCultureAnalytics Company
#

"""
Wrappers around sklearn's common cross validation methods.
"""

from sklearn.model_selection import GridSearchCV, StratifiedKFold, ParameterGrid


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


class SelectiveGridSearchCV(GridSearchCV):
    """SelectiveGridSearchCV

    By default, the original
    `sklearn.model_selection.GridSearchCV` runs through all possible
    combinations of hyperparamters through the estimator. This class allows
    dropping specific combinations od hyperparameters from the gridsearch.
    """

    def __init__(self, estimator, grid_exceptions=[], **kwargs):
        """__init__

        :param estimator: The sklearn estimator to be passed to grid search.
        (Same as the first parameter of GridSearchCV).
        :param grid_exceptions: List of dictionaries that represent
        combinations of parameterst that need to be omitted from the grid
        search.
        :param **kwargs: Other arguments to be passed to the grid search.
        """
        self.grid_exceptions = grid_exceptions
        super(SelectiveGridSearchCV, self).__init__(estimator, **kwargs)
        self.restricted_grid = list(ParameterGrid(self.param_grid))
        to_remove = []
        for exception in self.grid_exceptions:
            for combination in self.restricted_grid:
                if all(item in combination.items() for item in
                        exception.items()):
                    to_remove.append(combination)
        for removal in to_remove:
            self.restricted_grid.remove(removal)

    def fit(self, X, y=None, groups=None):
        """Run fit with all sets of parameters.

        Parameters
        ----------

        X : array-like, shape = [n_samples, n_features]
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.

        y : array-like, shape = [n_samples] or [n_samples, n_output], optional
            Target relative to X for classification or regression;
            None for unsupervised learning.

        groups : array-like, with shape (n_samples,), optional
            Group labels for the samples used while splitting the dataset into
            train/test set.
        """
        return self._fit(X, y, groups, self.restricted_grid)
