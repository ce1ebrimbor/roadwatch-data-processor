# tests/test.py
from data_prc.core import *
import unittest

class TableBaseTest(unittest.TestCase):


    def _read_file(self, path):
        return Table(path)


    def test_init(self):
        tb = self._read_file('tests/test_file.csv')
        self.assertIsNotNone(tb)
        self.assertEqual(tb.dataFrame.index.name, 'num_acc')

    def test_add_modifier(self):
        tb = self._read_file('tests/test_file.csv')
        modifiers = len(tb.modifiers)

        def dummyFunction(row):
            row['adr'] = 'modified'
            return row['adr']

        tb.addModifier('adr', dummyFunction)
        self.assertEqual(len(tb.modifiers), modifiers + 1)
