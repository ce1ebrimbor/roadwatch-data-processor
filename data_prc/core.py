#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
.. module:: core
   :platform: Unix, Windows
   :synopsis: Core functionalities for data processing.

.. moduleauthor:: Daniel SASU <daniel.sasu@mail.com>


"""

import pandas as pd
import numpy as np


class ColumnNotFoundException(Exception):
    """Exception raised when column is not found"""
    pass


class Table:
    """
    A generic table. This class is used to wrap a pandas data frame.
    """

    def __init__(self, path, dtype=None, sep=',', index='num_acc', encoding='latin-1', col_rename=[{'Num_Acc': 'num_acc'}]):
        """
        Initializes a Table using a csv file.

        :param path: csv file path
        :type path: str
        :param dtype: column data types
        :type dtype: dict
        :param sep: column separator
        :type sep: str
        :param index: index column
        :type index: str
        :param encoding: latin-1
        :type encoding: string

        """
        self.readCSV(path, sep=sep, dtype=dtype, index=index,
                     encoding=encoding, col_rename=col_rename)

    def _col_rename(self, map):
        """
        Renames columns

        :param map: a list of dict of the form { <old name>: <new name> }
        :type map: lst

        """
        for m in map:
            self.dataFrame.rename(columns=m, inplace=True)

    def readCSV(self, path, dtype, sep=',', index='num_acc', encoding='latin-1', col_rename=[{'Num_Acc': 'num_acc'}]):
        """
        Initializes a Table using a csv file.

        :param path: csv file path
        :type path: str
        :param dtype: column data types
        :type dtype: dict
        :param sep: column separator
        :type sep: str
        :param index: index column
        :type index: str
        :param encoding: latin-1
        :type encoding: string

        """
        self.dataFrame = pd.read_csv(
            path, dtype=dtype, encoding=encoding, sep=sep)
        self.validators = {}
        self.modifiers = {}
        self._col_rename(col_rename)

        if index in self.dataFrame.columns.values.tolist():
            self.dataFrame.set_index(index, inplace=True)

        self.columns = self.dataFrame.columns.tolist()

    def addModifier(self, column, function):
        """
        Adds a modifier which will be used to process a specific column
        A modifier can be used to add a column.

        :param column: a column name
        :type column: str
        :param function: a modifier function
        :type function: function

        """
        self.modifiers[column] = function

    def process(self):
        """
        Applies all the modifiers to dataFrame.

        """
        for proc in self.modifiers:
            self.dataFrame[proc] = self.dataFrame.apply(
                self.modifiers[proc], axis=1)

    def clean(self, col_lst):
        """
        Drops columns from the table

        :param col_lst: a list of columns to be dropped
        :type col_lst: lst

        """
        self.dataFrame = self.dataFrame.drop(col_lst, axis=1)

    def writeCSV(self, path):
        """
        Writes the table in a csv file.

        :param path: a file path
        :type path: str

        """
        self.dataFrame.to_csv(path)
