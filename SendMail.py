# -*- coding: utf-8 -*-
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

    def sendMail(self, to, url, siteName):
        msg = MIMEText(u'Die URL: %s hat sich geaendert' % (url))

        msg['Subject'] = u'[Ueberwachung] %s' % siteName
        msg['From'] = self.config['sender']
        msg['To'] = to

        s = smtplib.SMTP(self.config['server'])
        s.sendmail(self.config['sender'], [to], msg.as_string())
        s.quit()
