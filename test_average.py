import average
import unittest
import statistics

class test_average(unittest.TestCase):
  def test_average1(self):
    list = [1, 2, 3, 4, 5]
    self.assertEqual(average.average(list), 3)
  def test_average2(self):
    list = ["Jim", "Terry", "Bill"]
    self.assertEqual(average.average(list), 0)
  def test_average3(self):
    list = []
    self.assertRaises(statistics.StatisticsError, average.average(list))