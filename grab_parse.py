import requests
import lxml.html
import gzip
#method for reading straight xml
r= requests.get("http://smarkets.s3.amazonaws.com/oddsfeed.xml")
e = lxml.html.etree.parse(r.text.encode("ascii","ignore"))
print dir(e)

r = requests.get("http://thedataincubator-challenge.s3.amazonaws.com/HCHACdrgRBoVokdgdJNF/Badges.xml.gz")
with open("badges.xml.gz", "wb") as f:
  f.write(r.content())
g = gzip.open("badges.xml.gz","rb") 

with open("badges.xml","w") as f:
  f.write(g.read())

