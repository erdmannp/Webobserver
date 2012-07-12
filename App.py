'''
Created on 12.07.2012

@author: pe
'''
from ParseConfig import ParseConfig
from FetchSite import FetchSite
import os


class App():
    config = object
    fetcher = object
    path = os.path.abspath(os.path.dirname(__file__))
    tmpPath = path + '/tmp'

    def __init__(self):
        if not os.access(self.tmpPath, 755):
            try:
                os.mkdir(self.tmpPath)
                os.chmod(self.tmpPath, 755)

            except OSError:
                os.chmod(self.tmpPath, 755)
            except:
                raise

        self.config = ParseConfig()
        self.fetcher = FetchSite(self.config.getSites())

    def run(self):
        pass


if __name__ == '__main__':
    app = App()
    app.run()
