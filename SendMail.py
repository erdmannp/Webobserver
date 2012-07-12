'''
Created on 12.07.2012

@author: pe
'''
import smtplib
from email.mime.text import MIMEText


class SendMail(object):
    config = object

    def __init__(self, cfg):
        self.config = cfg
        msg = MIMEText("")

        msg['Subject'] = u'[Überwachung] %s' % textfile
        msg['From'] = me
        msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()