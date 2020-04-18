import urllib3

headers = {
  'token': 'ChlVriwCTmwJd2XMLZ2UwY1uovz2QbhoSqdlg9_wWnk'
}
http = urllib3.PoolManager()
request = http.request('GET', 'https://avwx.rest/api/station/kgfk', fields=headers)

print(request.data)
