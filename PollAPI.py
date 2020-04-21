#!/usr/bin/env python
import urllib3
import json

headers = {
    'Content-Type':'application/json',
    'token':'yourapikeyhere'
}
http = urllib3.PoolManager()
request = http.request('GET', 'https://avwx.rest/api/station/klns', fields=headers)
request2 = http.request('GET', 'https://avwx.rest/api/metar/klns', fields=headers)
request3 = http.request('GET', 'https://avwx.rest/api/taf/klns', fields=headers)

with open('Info.json', 'wb') as outfile1:
    outfile1.write(request.data)
with open('Metar.json', 'wb') as outfile2:
    outfile2.write(request2.data)
with open('TAF.json', 'wb') as outfile3:
    outfile3.write(request3.data)
