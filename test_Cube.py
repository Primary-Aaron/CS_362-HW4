import cube
import unittest

class test_cube(unittest.TestCase):
  def test1(self):
    self.assertEqual(cube.cubeIt("234sheesh"), 1000)
  def test2(self):
    self.assertEqual(cube.cubeIt("-20"), -1)
  def test3(self):
    self.assertEqual(cube.cubeIt("9999"), 999700029999)
  

