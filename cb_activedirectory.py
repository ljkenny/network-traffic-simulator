#!/usr/bin/python

import ldap

from cb_utils import write_log

server = "ldap.forumsys.com"
cred = "password"

AGENT_NAME = "ACTIVEDIRECTORY"

class ACTIVEDIRECTORY:
    def __init__(self):
        pass

    def ldap_search(keyword="", user="cn=read-only-admin",
                    base="dc=example,dc=com", filter="uid=*"):
        who = user + "," + base
        result_set = []
        timeout = 0
        count = 0

        try:
            l = ldap.open(server)
            l.simple_bind_s(who, cred)
        except ldap.LDAPError, error_message:
            print "Couldn't Connect. %s " % error_message

        try:
            result_id = l.search(base, ldap.SCOPE_SUBTREE, filter, None)

            while True:
                result_type, result_data = l.result(result_id, timeout)
                if (result_data == []):
                    break
                else:
                    if result_type == ldap.RES_SEARCH_ENTRY or \
                       result_type == ldap.RES_SEARCH_RESULT:
                        result_set.append(result_data)

                    if len(result_set) == 0:
                        print "No Results."
                        return

                for i in range(len(result_set)):
                    for entry in result_set[i]:
                        try:
                            count = count + 1
                            name = entry[1]['cn'][0]
                            surname = entry[1]['sn'][0]
                            email = entry[1]['mail'][0]
                            user = entry[1]['uid'][0]
                            #print "%d.\nName: %s %s\nE-mail: %s\nUsername: %s\n" %\
                                #    (count, name, surname, email, user)
                        except:
                            pass
            write_log(AGENT_NAME, "%d users found" % count)

        except ldap.LDAPError, error_message:
            print error_message
