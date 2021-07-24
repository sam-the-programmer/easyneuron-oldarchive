import inspect
import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from easyNeuron import *


class DataTester(unittest.TestCase):

    def test_cities(self):
        self.assertTrue(
            Data.load_cities()[:5] == ['South Elmira', 'South Trey', 'West Hobarttown', 'Mohrstad', 'Funkmouth'])
    

if __name__ == '__main__':
    unittest.main()
