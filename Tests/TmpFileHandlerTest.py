'''
Created on 12.07.2012

@author: pe
'''
import unittest
from TmpFileHandler import TmpFileHandler


class TmpFileHandlerTest(unittest.TestCase):

    def testTmpFileHandler(self):
        fh = TmpFileHandler("test")
        fh.setHash("123")
        tmp = fh.getHash()
        fh.delete()
        self.assertEquals(tmp, "123", "")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
