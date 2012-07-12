'''
Created on 12.07.2012

@author: pe
'''
import unittest
from ParseConfig import ParseConfig


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParseConfig(self):
        parser = ParseConfig()
        parser.getSites()
        parser.getGeneral()
        parser.getMailConfig()
        parser.getContacts()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
