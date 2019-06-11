import re
import urllib2
import random
import time
from sets import Set

from cb_utils import write_log

AGENT_NAME = "BROWSE"

class BROWSE:
    def __init__(self):
        pass

    def browse_now(self, url=""):
        generator = "http://www.randomwebsite.com/cgi-bin/random.pl"
        expr = '''href=["'](.[^"']+)["']'''

        childurls = []

        try:
            if not url:
                # Grab a random URL from the online generator
                request = urllib2.Request(generator)
                opener = urllib2.build_opener()
                result = opener.open(request)
                url = result.url

            url = url.strip("/")

            write_log(AGENT_NAME, " Browsing site: %s" % (url))

            # Scrape the random webpage and search for links
            for i in re.findall('''href=["'](.[^"']+)["']''', \
                                urllib2.urlopen(url).read(), re.I):
                if not i.startswith("http"):
                    continue

                # Use only the front page i.e. strip of sub-pages
                groups = i.split('/')
                childurl = groups[0] + "//" + groups[2]
                childurls.append(childurl)

                # Remove duplicates
                uniq = Set(childurls)

                # Pick one at random
                newurl = random.choice(list(uniq))

                if url == newurl:
                    newurl = ""

                return newurl

        except:
            # Catch 404 errors
            self.browse_now("")

    def browse(self, seconds):
        write_log(AGENT_NAME, "Browsing the web for %d seconds" % (seconds))

        url = ""
        start = time.time()
        while True:
            now = time.time()
            if now - start > seconds:
                return
            url = self.browse_now(url)

        
