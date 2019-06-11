#!/usr/bin/python

import smtplib
import imaplib
import logging
import sys

import subprocess
import email
import os

from cb_utils import write_log, enter_dumb_mode, leave_dumb_mode, is_dumb

AGENT_NAME = "EMAIL"

message = """
From: This Person <###USER###>
To: That Person <###TO###>
Subject: SMTP e-mail test
This is a test e-mail message.
"""

powershellexe = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"

class EMAIL:
    def __init__(self):
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)

        self.receivers  = '<###TO###>'
        self.username   = '<###USER###>'
        self.password   = '<###PASS###>'
        self.smtpserver = '<###URL###>'
        self.imapserver = '<###URL###>'
        self.inbox      = 'INBOX'

    def check_for_commands(self, imap, first_unread_msg):
        typee, msgparts = imap.fetch(first_unread_msg, '(RFC822)')
        emailbody = msgparts[0][1]

        if emailbody.find("CMD:ENTERDUMB") > 0:
            enter_dumb_mode()

        if emailbody.find("CMD:LEAVEDUMB") > 0:
            enter_dumb_mode()

    def send(self):
        server = self.open_smtp()
        server.sendmail(self.username, self.receivers, message)
        write_log(AGENT_NAME, "Successfully sent one email")
        server.quit()

    def read_and_click_attachment(self, imap, first_unread_msg):
        typee, msgparts = imap.fetch(first_unread_msg, '(RFC822)')
        emailbody = msgparts[0][1]
        mail = email.message_from_string(emailbody)
        numattach = 0

        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                #print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                #print part.as_string()
                continue

            filename = part.get_filename()
            if bool(filename):
                filepath = os.path.join(".", filename)
                numattach = numattach + 1
                fp = open(filepath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                if ".ps1" in filepath:
                    subprocess.call([powershellexe, ". \"" + filepath + "\";"])

        write_log(AGENT_NAME, "Read an email with %d attachment(s)" % numattach)

    def mark_as_read(self, imap, first_unread_msg):
        try:
            # Fetch and print first unread message
            typee, response = imap.fetch(first_unread_msg, '(UID BODY[TEXT])')
            if typee != 'OK':
                write_log(AGENT_NAME, "Failed to fetch email")

            # Mark it as read
            imap.store(first_unread_msg, '+FLAGS', '\Seen')
            write_log(AGENT_NAME, "Successfully read one email")
        except imap.error:
            write_log(AGENT_NAME, "Failed to read email")

    def read(self):
        imap = self.open_imap()
        status, response = imap.search(None, '(UNSEEN)')
        unread_msgs = response[0].split()
        first_unread_msg = unread_msgs[0]

        if len(unread_msgs) == 0:
            write_log(AGENT_NAME, "No mails to read")
            return

        self.check_for_commands(imap, first_unread_msg)

        if is_dumb():
            self.read_and_click_attachment(imap, first_unread_msg)
        else:
            self.mark_as_read(imap, first_unread_msg)

        self.close_imap(imap)

    def count_unread(self):
        imap = self.open_imap()
        status, response = imap.search(None, '(UNSEEN)')
        unread_msgs = response[0].split()

        write_log(AGENT_NAME, "%d unread emails" % len(unread_msgs))
        self.close_imap(imap)

        return len(unread_msgs)

    def open_imap(self):
        imap = imaplib.IMAP4_SSL(self.imapserver, 993)
        imap.login(self.username, self.password)
        imap.select(self.inbox)
        return imap

    def close_imap(self, imap):
        imap.close()
        imap.logout()

    def open_smtp(self):
        server = smtplib.SMTP_SSL(self.smtpserver, 465)
        server.login(self.username, self.password)
        return server
