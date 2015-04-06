#
# DCP product code
#
# (C) Copyright 2015-2016 Dataculture Analytics Company
# All right reserved.
#
# This file is confidential and NOT open source.  Do not distribute.
#


"""
A collection of miscellaneous utility functions.
"""

import pandas as pd


def colnames(filename, **kwargs):
    """
    Read the column names of a delimited file, without actually reading the
    whole file. This is simply a wrapper around `pandas.read_csv`, which reads
    only one row and returns the column names.

    Parameters:
    -----------

    filename: Path to the file to be read

    kwargs: Arguments to be passed to the `pandas.read_csv`

    """

    if 'nrows' in kwargs:
        UserWarning("The nrows parameter is pointless here. This function only"
                    "reads one row.")
        kwargs.pop('nrows')
    return pd.read_csv(filename, nrows=1, **kwargs).columns.tolist()


def get_vectorized_dict(df):
    """
    Given a dataframe, convert all columns to dict-vectorized array.
    """
    from sklearn.feature_extraction import DictVectorizer
    from scipy.sparse import hstack
    dv = DictVectorizer()
    X = []
    s = 0
    for col in df:
        s += df[col].nunique()
        x = dv.fit_transform([dict(value=f) for f in df[col]])
        X.append(x)
    X = hstack(X)
    assert X.shape[1] == s
    return X


def dataframe_query(df, query):
    """
    A more Pythonic way of querying a dataframe, instead of generating the
    sql-like string that the `pandas.DataFrame.query` method uses.

    Parameters:
    -----------

    `df`: The dataframe to be queried.

    `query`: A dictionary where each key must be a column in `df` and it's
    value is the value queried for.

    Returns: A dataframe with the queried results.

    """
    for k, v in query.iteritems():
        df = df[df[k] == v]
    return df
