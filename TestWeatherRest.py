import urllib3
import json

headers = {
  'token': 'ChlVriwCTmwJd2XMLZ2UwY1uovz2QbhoSqdlg9_wWnk'
}
http = urllib3.PoolManager()
request = http.request('GET', 'https://avwx.rest/api/station/kgfk', fields=headers)
request2 = http.request('GET', 'https://avwx.rest/api/metar/kgfk', fields=headers)

print(request.data)
with open('Info.txt', 'w') as outfile1:
    json.dump(str(request.data), outfile1)
print(request2.data)
with open('Metar.txt', 'w') as outfile2:
    json.dump(str(request2.data), outfile2)
