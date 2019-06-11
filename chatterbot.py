#!/usr/bin/python
#
#   a88888b. dP                  dP     dP                     dP                  dP   
#  d8'   `88 88                  88     88                     88                  88   
#  88        88d888b. .d8888b. d8888P d8888P .d8888b. 88d888b. 88d888b. .d8888b. d8888P 
#  88        88'  `88 88'  `88   88     88   88ooood8 88'  `88 88'  `88 88'  `88   88   
#  Y8.   .88 88    88 88.  .88   88     88   88.  ... 88       88.  .88 88.  .88   88   
#   Y88888P' dP    dP `88888P8   dP     dP   `88888P' dP       88Y8888' `88888P'   dP   

from optparse import OptionParser

import time
import socket

import cb_utils

import cb_dns
import cb_email
#import cb_shares
import cb_twitter
import cb_translate
import cb_browse_web
import cb_download_file
import cb_activedirectory

#from cb_translation_spider import translate_paragraph, fetch_paragraph
#from cb_web_browser_spider import spider_run_invoker

AGENT_NAME = "CHATTERBOT"

def populate_options():
    parser = OptionParser(usage="Usage: %prog [options]")

    parser.add_option("--verbose", "-v", dest="verbose",
                      action="store_true", default=False,
                      help="Be verbose")

    (options, args) = parser.parse_args()

    return options

def main():
    options = populate_options()

    hostname = socket.gethostname()
    print "Running on Host: %s" % hostname

    # Send a random search to a search engine
    browse = cb_browse_web.BROWSE()
    browse.browse(8)

    # Tweet a post to Twitter
    tweet = cb_twitter.TWITTER()
    tweet.post()

    # Download a file
    dl = cb_download_file.DOWNLOADFILE()
    dl.download()

    # Use google.co.uk/translate to translate a paragraph from English to another language
    # DNS resolve a random website URL
    translate = cb_translate.TRANSLATE()
    translate.translate()

    # DNS resolve a random website URL
    dns = cb_dns.DNS()
    dns.resolve()

    # Send an email
    email = cb_email.EMAIL()
    email.send()
    time.sleep(3)

    # Read all emails
    unread = email.count_unread()
    for i in xrange(unread):
        email.read()

    # HACK HACK HACK
    return

    # Active Directory serach
    ad = cb_activedirectory.ACTIVEDIRECTORY()
    ad.ldap_search()

    '''
    # Mount shares
    shares = cb_shares.SHARES()

    # Click on any URL contained in the search engine response

    # Lookup a random English word on Dictionary.com
    # Download a text file from the Internet and store on the H:\ drive
    # Copy a file from the team share (J:\ network drive) to the H:\
    # Create a word file / pdf with random content and save the J:\ drive
    # Write a file to a DropBox / OneDrive
    # Render a map based on latitude / longitude on Bing Maps
    # Any other task to generate typical LAN traffic
    # Resolve group memberships in AD
    '''

if __name__ == "__main__":
    main()
