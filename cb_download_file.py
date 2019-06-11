#!/usr/bin/python

import urllib
import random

from cb_utils import write_log

#files = [ 'http://www.oxfordmartin.ox.ac.uk/downloads/academic/The_Future_of_Employment.pdf',
#          'http://credo.stanford.edu/documents/NCSS%202013%20Final%20Draft.pdf',
#          'http://cep.lse.ac.uk/pubs/download/dp1350.pdf',
#          'http://dromorehighschool.co.uk/wp-content/uploads/EN086-Downloading-Microsoft-Office-for-Staff.pdf' ]
files = [ 'http://cep.lse.ac.uk/pubs/download/dp1350.pdf' ]

AGENT_NAME = "DOWNLOAD"

class DOWNLOADFILE:
    def __init__(self):
        pass

    def download(self):
        download = random.choice(files)

        try:
            urllib.urlretrieve(download, "delme.pdf")
        except:
            write_log(AGENT_NAME, "Failed to download: %s" % (download))
            pass

        write_log(AGENT_NAME, "Downloaded file: %s" % (download))

        
