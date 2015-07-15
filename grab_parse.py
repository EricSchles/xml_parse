import requests
import lxml.html

r= requests.get("http://smarkets.s3.amazonaws.com/oddsfeed.xml")
e = lxml.html.etree.parse(r.text.encode("ascii","ignore"))
print dir(e)
