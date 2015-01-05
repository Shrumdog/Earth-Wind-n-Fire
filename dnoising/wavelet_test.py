'''
Created on Sep 11, 2014

@author: Ian
'''
import unittest
import wavelet_proto


class Test(unittest.TestCase):


    def setUp(self):
        proto = wavelet_proto.wave([4.0, 6.0, 2.0, 10.0, 8.0, 8.0, 6.0, 4.0], 1)


    def tearDown(self):
        pass


    def testDiffs(self):
        assert proto.get_diffs(1) == [-2.0, -8.0, 0.0, 2.0]


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()