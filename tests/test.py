# tests/test.py
from data_prc.core import *
import unittest

class TableBaseTest(unittest.TestCase):


    def _read_file(self, path):
        return Table(path)


    def test_init(self):
        tb = self._read_file('tests/test_file.csv')
        self.assertIsNotNone(tb)
