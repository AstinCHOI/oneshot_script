import os
import requests
import sys

urls = ''
with open(sys.argv[1]) as f:
	urls = f.read()

urls = urls.split('\n')
for url in urls:
	res = requests.get(url, allow_redirects=False)
	try:
		print(res.headers['Location'])
	except:
		print("## " + url)
