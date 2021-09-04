import httplib
import base64

h = '192.168.0.160'
u = 'ric'
p = 'passw0rd'

authToken = base64.encodestring('%s:%s'% (u, p)).replace('\n', '')
print(authToken)

req = httplib.HTTP(h)
req.putrequest("GET", "/protected/index.html")
req.putheader("Host", h)
req.putheader("Authorization", "Basic %s"% authToken)
req.endheaders()
req.send("")

statusCode, statusMsg, _headers = req.getreply()
print("Response:", statusMsg)