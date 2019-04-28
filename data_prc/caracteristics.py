#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
.. module:: caracteristics
   :platform: Unix, Windows
   :synopsis: A list of modifiers for 'caracteristiques files'

.. moduleauthor:: Daniel SASU <daniel.sasu@mail.com>

"""

import pandas as pd
import numpy as np
import datetime

def put_gps_lat(row):
    """
    Format latitude as a float.

    :param row: a data frame row
    :type row: pandas.Series
    :returns: processed value.

    """
    if(row['lat'] == 0 and row['long'] == 0):
        row['long'] = 0
    else:
       row['lat'] = row['lat'] / 100000.0

    return row['lat']



def put_gps_long(row):
    """
    Format longitude as a float.

    :param row: a data frame row
    :type row: pandas.Series
    :returns: processed value.

    """
    if(row['lat'] == 0 and row['long'] == 0):
        row['long'] = 0
    else:
       row['long'] = row['long'] / 100000.0

    return row['long']



def put_timestamp(row):
    """
    Converts the date to a timestamp.

    :param row: a data frame row
    :type row: pandas.Series
    :returns: processed value.

    """
    return create_timestamp(2000 + row['an'], row['mois'], row['jour'], row['hrmn']// 100, row['hrmn'] % 100)


def put_insee(row):
    """
    Formats zip city zip code.

    :param row: a data frame row
    :type row: pandas.Series
    :returns: processed value.

    """
    return str(row['dep'])[:-1] + str(row['com'])

def _create_timestamp(year, month, day, hour, min):
    """
    Converts integers to a timestmp

    """
    if year is None or month is None or day is None or hour is None or min is None:
        return None
    else:
        entry = datetime.datetime(year, month, day, hour, min)

        return entry
