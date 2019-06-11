#!/usr/bin/python

import urllib2
import socket

from cb_utils import write_log

AGENT_NAME = "DNS"

class DNS:
    def __init__(self):
        pass

    def resolve(self):
        generator = "http://www.randomwebsite.com/cgi-bin/random.pl"
        try:
            request = urllib2.Request(generator)
            opener = urllib2.build_opener()
            result = opener.open(request)
            url = result.url[7:].split("/",1)[0]
            if url.startswith("www."):
                url = url[4:]
            ip = socket.gethostbyname(url)
            write_log(AGENT_NAME, "Resolved %s to %s" % (url, ip))
        except:
            self.resolve()
