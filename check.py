#! /usr/bin/env python

# "Copright 2012, Severin Kistner"

# rough flow:
#    $domain=”please enter your domain name”
#    $XMPP-SERVER=”host -t SRV _xmpp-server._tcp.$domain”
#    $API-SERVER=”host -t SRV _buddycloud-api-server._tcp.$domain”
#    $WEBCLIENT=”host -t SRV _buddycloud-webclient._tcp.$domain”
#    # check the buddycoud-server is also in DNS.
#    $BC_COMPONENT=”buddycloud.$XMPP-SERVER”
#    $BC_ANON=”anon.$XMPP-SERVER”
#    $BC_MEDIA=”media.$XMPP-SERVER”
#    $BC_PUSHER=”pusher.$XMPP-SERVER”
#    $BC_TOPICS=”topics.$XMPP-SERVER”
#    try to connect to the $XMPP-SERVER
#    try to register a user on $XMPP-SERVER
#    try to remove that user from $XMPP-SERVER
#    try to connect as an anonymous user on $XMPP-SERVER
#    DISCO for the buddycloud component on $XMPP-SERVER
#    try to connect to the buddycloud component on $XMPP-SERVER
#    try to connect to $API-SERVER server on HTTP
#    via $API-SERVER, try to retrieve a known open channel from a remote domain
#    try to connect to the media server on XMPP
#    try to connect to the media server on HTTP
#    try to retrieve a known avatar
#    try to retrieve a known piece of media
#    xmpp ping the pusher component (don’t know how else to test it)
#    grep for a known string in config.js from https://$WEBCLIENT/config.js



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