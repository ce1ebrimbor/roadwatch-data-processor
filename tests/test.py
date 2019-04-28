# tests/test.py
from data_prc.core import *
import unittest

class TableTest(unittest.TestCase):

    def _dummyModifierFunction(self, row):
        row['adr'] = 'modified'
        return row['adr']

    def test_init(self):
        tb = Table('tests/test_file.csv')
        self.assertIsNotNone(tb)
        self.assertEqual(tb.dataFrame.index.name, 'num_acc')

    def test_add_modifier(self):
        tb = Table('tests/test_file.csv')
        modifiers = len(tb.modifiers)

        tb.addModifier('adr', self._dummyModifierFunction)
        self.assertEqual(len(tb.modifiers), modifiers + 1)

    def test_col_rename(self):
        tb = Table('tests/test_file.csv', col_rename=[])
        self.assertTrue('adr' in tb.dataFrame.columns.values.tolist())
        tb = Table('tests/test_file.csv', col_rename=[{'adr': 'ADR'}])
        self.assertTrue('ADR' in tb.dataFrame.columns.values.tolist())

    def test_clean(self):
        tb = Table('tests/test_file.csv')
        self.assertTrue('adr' in tb.dataFrame.columns.values.tolist())
        self.assertTrue('gps' in tb.dataFrame.columns.values.tolist())
        tb.clean(['gps', 'adr'])
        self.assertFalse('adr' in tb.dataFrame.columns.values.tolist())
        self.assertFalse('gps' in tb.dataFrame.columns.values.tolist())

    def test_process(self):
        tb = Table('tests/test_file.csv')
        tb.addModifier('adr', self._dummyModifierFunction)
        tb.process()
        self.assertTrue('modified' in tb.dataFrame['adr'].tolist())
