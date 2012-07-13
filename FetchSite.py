'''
Created on 12.07.2012

@author: pe
'''
import urllib2
import hashlib


class FetchSite():
    data = ""

    def __init__(self, site):
        try:
            f = urllib2.urlopen(site)
            self.data = f.read()
            f.close()
        except ValueError:
            raise

    def getData(self):
        return self.data

    def getHash(self):
        try:
            return hashlib.sha1(self.data).hexdigest()
        except:
            raise

if __name__ == '__main__':
    pass
