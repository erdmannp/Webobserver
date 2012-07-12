'''
Created on 12.07.2012

@author: pe
'''
import urllib
import hashlib


class FetchSite():
    sites = object

    def __init__(self, sites):
        self.sites = sites

    def process(self, site):
        data = ""

        try:
            f = urllib.urlopen(self.sites[site]['url'])
            data = f.read()
            f.close()
        except ValueError:
            raise

        return data

    def getHash(self, site):
        try:
            return hashlib.sha1(self.process(site))
        except:
            raise

if __name__ == '__main__':
    pass
