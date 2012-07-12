'''
Created on 12.07.2012

@author: pe
'''
import os
import stat


class TmpFileHandler(object):
    path = os.path.abspath(os.path.dirname(__file__))
    tmpPath = path + '/tmp'
    f = object

    def __init__(self, f):
        self.f = f
        if not os.access(self.tmpPath, os.W_OK) and not os.access(self.tmpPath, os.R_OK):
            try:
                os.mkdir(self.tmpPath)
                os.chmod(self.tmpPath, stat.S_IRWXU)

            except OSError:
                os.chmod(self.tmpPath, stat.S_IRWXU)
            except:
                raise

    def getHash(self):
        try:
            fp = open(os.path.join(self.tmpPath, self.f), 'r')
            return fp.read()
        except:
            self.setHash(' ')
            return

    def setHash(self, h):
        fp = open(os.path.join(self.tmpPath, self.f), 'w')
        fp.write(h)
        fp.close()

    def delete(self):
        os.unlink(os.path.join(self.tmpPath, self.f))

