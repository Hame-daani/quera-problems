import unittest
import csv
import sys
sys.path.append('../Initial_project')
from solution import process


class Test(unittest.TestCase):
    def test_1(self):
        my_list = ['sample1.json', 'sample2.json']
        process(my_list)
        with open('ans.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        correct_data = [['1', '3'], ['3', '1']]
        self.assertEqual(correct_data, data)
        
        
if __name__ == '__main__':
    unittest.main()