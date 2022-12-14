import unittest
from super_algos import find_min ,sum_all ,find_possible_strings


class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        #ind_min(element)
        self.assertEqual(find_min([]),-1)
    def test_NeG_NO(self):
        self.assertEqual(find_min([1,2,3,-4]),-4)
    def test_if_int(self):
        self.assertEqual(find_min([1,"2",3,4]),-1)
    def Test_IF_one_iteam(self):
        self.assertEqual(find_min([1]),1)
    def test_correct(self):
        self.assertEqual(find_min([1,2,3,4]),1)