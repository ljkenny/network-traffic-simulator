#!/usr/bin/python

import urllib2
import socket

class DNS:
    def __init__(self):
        self.generator = "http://www.randomwebsite.com/cgi-bin/random.pl"

    def resolve_one(self):
        try:
            request = urllib2.Request(self.generator)
            opener = urllib2.build_opener()
            result = opener.open(request)
            url = result.url[7:].split("/",1)[0]
            if url.startswith("www."):
                url = url[4:]
            ip = socket.gethostbyname(url)
            print "DNS: Resolved " + result.url + " to " + ip
        except:
            self.resolve_one()
