#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Certerator 0.1-pre1
#  Stuart Morgan <stuart.morgan@mwrinfosecurity.com> @ukstufus
#
#  This tool will parse a Windows Registry Editor 'reg' file of a certificate,
#  and produce a command line representation of it.
#

import os
import sys
import re

# Read the .reg file from STDIN
regfile = sys.stdin.readlines()
   
reg_path = ""
reg_key = ""
reg_binary = ""

# Loop through each line
for line in regfile:

    # Try to match the location
    header = re.search(r'^\[([^\\]+\\SOFTWARE\\Microsoft\\SystemCertificates\\[^\\]+\\Certificates)\\([A-Z0-9]+)\]\s*$', line)
    if header != None:
        reg_path = header.group(1)
        reg_key = header.group(2)

    # Now match the rest of the file
    body = re.search(r'^\s*(?:"Blob"=hex:)?\s*([a-z0-9,]+)[,\\]*\s*$', line)
    if body != None:
        reg_binary += body.group(1).replace(',','')

if reg_path and reg_key and reg_binary:
    print "[+] Path: "+reg_path
    print "[+] Key: "+reg_key
    print "[+] Binary: "+reg_binary

    print "\n"

