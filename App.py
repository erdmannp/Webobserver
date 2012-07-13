from __future__ import print_function
'''
Created on 12.07.2012

@author: pe
'''
from ParseConfig import ParseConfig
from FetchSite import FetchSite
from SendMail import SendMail
from TmpFileHandler import TmpFileHandler
from hashlib import sha1


class App():
    config  = object
    mail    = object
    debug   = False

    def __init__(self):
        self.config = ParseConfig()
        self.mail = SendMail(self.config.getMailConfig())
        self.debug = self.config.getGeneral()['debug']

    def run(self):
        if self.debug:
            print("Running in Debug Mode")

        for site in self.config.getSites():
            try:
                regex = self.config.getSites()[site]['regex']
            except KeyError:
                regex = None

            url = self.config.getSites()[site]['url']

            obj = TmpFileHandler(site)
            fetcher = FetchSite(url)

            if regex is not None:
                if self.debug:
                    print("Using Regex for " + site)
                fetcher.useRegex(regex)
                if self.debug:
                    print("Regex Result (first 100 chars): " + fetcher.getData()[0:100])

            if obj.getHash() is 'init':
                if self.debug:
                    print("First Time fetching " + site)
                obj.setHash(fetcher.getHash())
                break

            if obj.getHash() != fetcher.getHash():
                if self.debug:
                    print(
                          "Hash from File: %s \nHash from Site: %s" %
                          (obj.getHash(), fetcher.getHash())
                          )

                # Mail senden und neuen Hash speichern
                obj.setHash(fetcher.getHash())

                for contact in self.config.getContacts():
                    to = self.config.getContacts()[contact]['email']
                    if site in  self.config.getContacts()[contact]['sites']:
                        self.mail.sendMail(to, url, site)

if __name__ == '__main__':
    app = App()
    app.run()
