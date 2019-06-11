#!/usr/bin/python

import smtplib

class SMTP:
    def __init__(self):
        self.sender = '<###EMAIL###>'
        self.password = '<###PASS###>'
        self.receivers = ['<###EMAIL###>']

    def send_one(self):
        message = """From: This Person <<###EMAIL###>>
        To: That Person <<###EMAIL###>>
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receivers, message)
            print "Successfully sent email"
        except smtplib.SMTPException:
            print "Error: unable to send email"

    def read_one(self):
        pass

    def count_unread(self):
        pass
