import urllib3
import json

headers = {
    'Content-Type':'application/json',
    'token':'ChlVriwCTmwJd2XMLZ2UwY1uovz2QbhoSqdlg9_wWnk'
}
http = urllib3.PoolManager()
request = http.request('GET', 'https://avwx.rest/api/station/kgfk', fields=headers)
request2 = http.request('GET', 'https://avwx.rest/api/metar/kgfk', fields=headers)
request3 = http.request('GET', 'https://avwx.rest/api/taf/kgfk', fields=headers)

with open('Info.json', 'wb') as outfile1:
    outfile1.write(request.data)
with open('Metar.json', 'wb') as outfile2:
    outfile2.write(request2.data)
with open('TAF.json', 'wb') as outfile3:
    outfile3.write(request3.data)
