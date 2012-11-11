#! /usr/bin/env python

# "Copright 2012, Severin Kistner"

import dns.resolver
import logging
from optparse import OptionParser
import requests

parser = OptionParser()
parser.add_option("-d", "--domain", dest="domain",
                  help="insert domain to check here", metavar="example.com")
parser.add_option("-v", "--verbose", dest="verbose",
				  action="store_true", default=False,
                  help="show logging messages", metavar="example.com")

(options, args) = parser.parse_args()

if options.verbose:
	logging.basicConfig(level=logging.INFO)

try:
	answers = dns.resolver.query("_xmpp-server._tcp." + options.domain, "srv")
	addresses = {}
	intmax = 0
	for answer in answers:
	    intmax += answer.priority
	    addresses[intmax] = (answer.target.to_text()[:-1],
	        answer.port)
except:
	print "Fail: Check your DNS"

logging.info(" XMPP-Server: " + addresses[5][0] + ":" + str(addresses[5][1]))


print "Success"