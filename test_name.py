import unittest
import name_full

class test_name(unittest.TestCase):
  def test1(self):
    self.assertEqual(name_full.fullName("Aaron", "Hardwick"), "Aaron Michael Hardwick")
  def test2(self):
    self.assertEqual(name_full.fullName(1, 2), "1 Ted 2")
  def test3(self):
    self.assertEqual(name_full.fullName("", ""), " Ted ")