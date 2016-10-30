#!/usr/bin/python
import subprocess, urllib, random, re

def getblocks():
    r = urllib.urlopen("URL_FOR_PAGE").read()
    x = r.split('"')
    result = []
    for block in x:
        if re.search('FILE_EXTENSION', block):
            result.append(block)
    return result

line = lambda x: ['curl', '-o', 'curl_test' + str(x) + '.jpg',
                  "URL_FOR_DOMAIN" + str(x)]

while 1:
    blocks = getblocks()
    for block in blocks:
        print block
        subprocess.Popen(line(block)).wait()
