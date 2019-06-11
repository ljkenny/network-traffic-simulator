#!/usr/bin/python

from cb_utils import write_log
from win_unc import DiskDrive, UncDirectory, UncDirectoryConnection
from win_unc import UncDirectoryMount, UncCredentials

AGENT_NAME = "UNC_SHARES"

class SHARES:
    def __init__(self):
        pass

    def mount_share_from_windows(self):
        # Mount share to Z: driver with authorization
        creds = UncCredentials('<###USER###>>>', '<###PASS###>')
        authz_unc = UncDirectory(r'\\<###SERVER_IP###>\share1\file.txt', creds)

        mnt = UncDirectoryMount(authz_unc, DiskDrive('Z:'))
        mnt.mount()
        print 'Mounted?', mnt.is_mounted()
        mnt.unmount()

    def mount_share_from_linux(self):
        pass

#fp = open(r'\\<###SERVER_IP###>\share1\file.txt', 'r')
#print fp.read()
#fp.close()
