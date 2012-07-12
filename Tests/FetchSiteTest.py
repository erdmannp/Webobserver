'''
Created on 12.07.2012

@author: pe
'''
import unittest
from FetchSite import FetchSite


class FetchSiteTest(unittest.TestCase):

    def testFetchSite(self):
        fs = FetchSite({u'Seitenname': {u'url': u'http://google.de', u'type': u'http'}})
        fs.process('Seitenname')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
