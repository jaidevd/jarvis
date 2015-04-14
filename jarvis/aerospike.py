#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""Tools for pushing pandas dataframes into aerospike servers."""

import aerospike


class DataFrameExporter(object):

    def __init__(self, namespace=None, dataframe=None, set_name=None,
                 hostname=None, port=3000):
        self.namespace = namespace
        self.dataframe = dataframe
        self.set_name = set_name
        self.hostname = hostname
        self.port = port

    def run(self):
        client = aerospike.client({'hosts': (self.hostname, self.port)})
        client = client.connect()
        for i in self.dataframe.index:
            self.client.put((self.namespace, self.set_name, i),
                            self.dataframe.ix[i].to_dict())
        self.client.close()

if __name__ == '__main__':
    from pysemantic import Project
    vf = Project("vfirst")
    mtlogs = vf.load_dataset("mtlogs")
    exporter = DataFrameExporter(namespace="vfirst", dataframe="vfirst",
                                 set_name="mtlogs", hostname="localhost")
    exporter.run()
