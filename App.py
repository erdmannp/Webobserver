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
    fetcher = object
    mail    = object

    def __init__(self):
        self.config = ParseConfig()
        self.fetcher = FetchSite(self.config.getSites())
        self.mail = SendMail(self.config.getMailConfig())

    def run(self):
        for site in self.config.getSites():
            url = self.config.getSites()[site]['url']
            obj = TmpFileHandler(site)
            if obj.getHash() is not self.fetcher.getHash(site):
                # Mail senden und neuen Hash speichern
                obj.setHash(sha1(site).hexdigest())

                for contact in self.config.getContacts():
                    to = self.config.getContacts()[contact]['email']
                    if site in  self.config.getContacts()[contact]['sites']:
                        self.mail.sendMail(to, url, site)

if __name__ == '__main__':
    app = App()
    app.run()
