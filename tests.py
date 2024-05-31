import unittest
import sys

from dictionaries_practice import test


class TestDictionaryProblems(unittest.TestCase):

  def test_upper(self):
    self.assertDictEqual(test, { 'import': 'import unitest'})

  def test_upper_2(self):
    self.assertDictEqual(test, { 'import': 'import unitest'})

if __name__ == '__main__':
  failfast = len(sys.argv) > 1 and sys.argv[1] == 'ff'
  unittest.main(failfast=failfast)
