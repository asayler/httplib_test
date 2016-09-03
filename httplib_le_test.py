#! /usr/bin/env python

import sys
import ssl

### httplib Tests ###

import httplib
print("### Testing with httplib and python {} ###".format(sys.version))

# Test Good LE
print("+ Testing properly configured LE Site +")
conn = httplib.HTTPSConnection("www.andysayler.com")
conn.request("GET", "/")
res = conn.getresponse()
print("    status = {}".format(res.status))
data = res.read()
print("    len = {}".format(len(data)))

# Test Moodle
print("+ Testing CU Main Moodle +")
conn = httplib.HTTPSConnection("moodle.cs.colorado.edu")
conn.request("GET", "/")
res = conn.getresponse()
print("    status = {}".format(res.status))
data = res.read()
print("    len = {}".format(len(data)))

# Test SDR
print("+ Testing CU SDR Moodle +")
conn = httplib.HTTPSConnection("sdr.cs.colorado.edu")
conn.request("GET", "/")
res = conn.getresponse()
print("    status = {}".format(res.status))
data = res.read()
print("    len = {}".format(len(data)))

# Test Bad Chain
print("+ Testing incomplete-chain.badssl.com +")
conn = httplib.HTTPSConnection("incomplete-chain.badssl.com")
try:
    conn.request("GET", "/")
except ssl.SSLError:
    print("    SSL Verification Error (Expected)")
else:
    raise Exception("Incomplete chain failed to raise error")


### httplib2 Tests ###

import httplib2
print("### Testing with httplib2 ({}) and python {} ###".format(httplib2.__version__, sys.version))

# Test Good LE
print("+ Testing properly configured LE Site +")
print("    Skipping test -- No SNI support in httplib2")
print("    See https://github.com/jcgregorio/httplib2/issues/233")
# h = httplib2.Http()
# res, content = h.request("https://www.andysayler.com/")
# print("    status = {}".format(res.status))
# print("    len = {}".format(len(content)))

# Test Moodle
print("+ Testing CU Main Moodle +")
h = httplib2.Http()
res, content = h.request("https://moodle.cs.colorado.edu/")
print("    status = {}".format(res.status))
print("    len = {}".format(len(content)))

# Test SDR
print("+ Testing CU SDR Moodle +")
h = httplib2.Http()
res, content = h.request("https://sdr.cs.colorado.edu/")
print("    status = {}".format(res.status))
print("    len = {}".format(len(content)))

# Test Bad Chain
print("+ Testing incomplete-chain.badssl.com +")
h = httplib2.Http()
try:
    res, content = h.request("https://incomplete-chain.badssl.com/")
except httplib2.SSLHandshakeError:
    print("    SSL Verification Error (Expected)")
else:
    raise Exception("Incomplete chain failed to raise error")
