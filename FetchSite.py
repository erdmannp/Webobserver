from __future__ import print_function
'''
Created on 12.07.2012

@author: pe
'''
import urllib2
import hashlib
import re
from sys import stderr


class FetchSite():
    data = ""

    def __init__(self, site):
        try:
            f = urllib2.urlopen(site)
            self.data = f.read()
            f.close()
        except urllib2.URLError:
            print("URLError Failure, could not open: %s" %(site), file=stderr)
        except ValueError:
            raise

    def useRegex(self, regex):        
        rtmp = re.findall(regex, self.data)
        tmp = ""
        
        if len(rtmp) > 0:
            for i in rtmp:
                tmp += i
        else:
            print()
            print("Failure in Regex, i'm using the default data", file=stderr)       

        self.data = tmp


    def getData(self):
        return self.data

    def getHash(self):
        try:
            return hashlib.sha1(self.data).hexdigest()
        except:
            raise

if __name__ == '__main__':
    pass
