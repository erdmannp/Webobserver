'''
Created on 12.07.2012

@author: pe
'''
import unittest
from FetchSite import FetchSite


class FetchSiteTest(unittest.TestCase):

    def testFetchSite(self):
        fs = FetchSite('http://www.uni-notebooks.net/ThinkPad-T420s-4173W15-4173CTO.3480.0.html')
        print fs.getData()
        print fs.getHash()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
