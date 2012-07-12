'''
Created on 12.07.2012

@author: pe
'''
import json
import os


class ParseConfig():
    config = object

    def __init__(self):
        cfgfo = file(os.path.abspath(os.path.dirname(__file__) + '/config.json'), 'r')
        self.config = json.loads(cfgfo.read())
        # Check for default Config File Layout
        try:
            self.config['sites']
            self.config['mailserver']
            self.config['contacts']
        except:
            raise

    def getSites(self):
        if len((self.config['sites'])) > 0:
            return self.config['sites']
        else:
            raise

    def getMailConfig(self):
        if len((self.config['mailserver'])) == 2:
            return self.config['mailserver']
        else:
            raise

    def getGeneral(self):
        if len((self.config['general'])) > 0:
            return self.config['general']
        else:
            raise

    def getContacts(self):
        if len((self.config['contacts'])) > 0:
            return self.config['contacts']
        else:
            raise

if __name__ == '__main__':
    pass