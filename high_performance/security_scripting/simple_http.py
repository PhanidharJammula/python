import http.client

h = http.client.HTTPConnection("www.google.com")
h.request('GET', '/')
data = h.getresponse()

print(data.code)
text = data.readlines()

for i in text:
    print(i)