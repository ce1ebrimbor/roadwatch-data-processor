# tests/test.py
from data_prc.core import *
import unittest


def _dummyModifierFunction(row):
    row['adr'] = 'modified'
    return row['adr']


class TableTest(unittest.TestCase):

    def test_init(self):
        tb = Table('tests/test_file.csv')
        self.assertIsNotNone(tb)

    def test_add_modifier(self):
        tb = Table('tests/test_file.csv')
        modifiers = len(tb.modifiers)

        tb.addModifier('adr', _dummyModifierFunction)
        self.assertEqual(len(tb.modifiers), modifiers + 1)

    def test_col_rename(self):
        tb = Table('tests/test_file.csv', col_rename=[])
        self.assertTrue('adr' in tb.dataFrame.columns.values.tolist())
        tb.col_rename([{'adr': 'ADR'}])
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
        tb.addModifier('adr', _dummyModifierFunction)
        tb.process()
        self.assertTrue('modified' in tb.dataFrame['adr'].tolist())

    def test_process_generic(self):
        df = process_generic_file('tests/test_file.csv', index='num_acc',
                                  encoding='latin-1', sep=',', dtype=None,
                                  col_rename=[{'Num_Acc': 'num_acc'}, {'adr': 'ADR'}, {'gps': 'GPS'}],
                                  cols_formatted=['ADR', 'GPS'], modifiers={'ADR': _dummyModifierFunction},
                                  drop_cols=['int', 'lat', 'long'])
        self.assertIsNotNone(df)
        self.assertEqual(df.index.name, 'num_acc')
        self.assertTrue('ADR' in df.columns.values.tolist())
        self.assertTrue('GPS' in df.columns.values.tolist())
        self.assertTrue('modified' in df['ADR'].tolist())
        self.assertFalse('int' in df.columns.values.tolist())
        self.assertFalse('lat' in df.columns.values.tolist())
        self.assertFalse('long' in df.columns.values.tolist())
