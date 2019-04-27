#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
.. module:: core
   :platform: Unix, Windows
   :synopsis:

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

    def __init__(self, path, dtype=None, sep=',', index='num_acc', encoding='latin-1'):
        """
        Initializes a Table using a csv file.

        :param path: csv file path
        :type path: str
        :param dtype: column data types
        :type dtype: dict
        :param sep: column separator
        :type sep: sep
        :param index: index column
        :type index: str
        :param encoding: latin-1
        :type encoding: string
        """
        self.readCSV(path, sep=sep, dtype=dtype, index=index, encoding=encoding)


    def readCSV(self, path, dtype, sep=',', index='num_acc', encoding='latin-1'):
        """
        Initializes a Table using a csv file.

        :param path: csv file path
        :type path: str
        :param dtype: column data types
        :type dtype: dict
        :param sep: column separator
        :type sep: sep
        :param index: index column
        :type index: str
        :param encoding: latin-1
        :type encoding: string
        """
        self.dataFrame = pd.read_csv(path, dtype=dtype, encoding=encoding, sep=sep)
        self.validators = {}
        self.modifiers = {}
        if index == 'num_acc':
            self.dataFrame.rename(columns={'Num_Acc': 'num_acc'}, inplace=True)
        else:
            self.dataFrame.rename(columns={'Code INSEE': 'code_insee'}, inplace=True)
            self.dataFrame.rename(columns={'Code Postal': 'code_postal'}, inplace=True)
            self.dataFrame.rename(columns={'Commune': 'commune'}, inplace=True)
            self.dataFrame.rename(columns={'Département': 'dep'}, inplace=True)
            self.dataFrame.rename(columns={'Région': 'region'}, inplace=True)
            self.dataFrame.rename(columns={'Statut': 'statut'}, inplace=True)
            self.dataFrame.rename(columns={'Altitude Moyenne': 'altitude_moyenne'}, inplace=True)
            self.dataFrame.rename(columns={'Superficie': 'superficie'}, inplace=True)
            self.dataFrame.rename(columns={'Population': 'population'}, inplace=True)
            self.dataFrame.rename(columns={'ID Geofla': 'id_geofla'}, inplace=True)
            self.dataFrame.rename(columns={'Code Commune': 'code_commune'}, inplace=True)
            self.dataFrame.rename(columns={'Code Canton': 'code_canton'}, inplace=True)
            self.dataFrame.rename(columns={'Code Arrondissement': 'code_arrondissement'}, inplace=True)
            self.dataFrame.rename(columns={'Code Département': 'code_dep'}, inplace=True)
            self.dataFrame.rename(columns={'Code Région': 'code_region'}, inplace=True)

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


    def writeCSV(self, path):
        """
        Writes the table in a csv file.

        :param path: a file path
        :type path: str
        """
        self.dataFrame.to_csv(path)
