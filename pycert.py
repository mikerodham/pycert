#!/usr/bin/env python

import sys, ssl, socket

host = sys.argv[1]

def connect_to_socket():
    context = ssl.create_default_context()

    skt = context.wrap_socket(socket.socket(), server_hostname=host)
    skt.connect((host, 443))
    cert = skt.getpeercert()

    return cert

cert = connect_to_socket()

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']

print("""
/**************************************/
/*    github.com/mikerodham/pycert    */
/**************************************/

SUBJECT: %s
Issued to: %s
Valid From: %s
Valid Until: %s

ISSUER: %s
"""
% (
    host,
    issued_to,
    cert['notBefore'],
    cert['notAfter'],
    issued_by
  )
)
