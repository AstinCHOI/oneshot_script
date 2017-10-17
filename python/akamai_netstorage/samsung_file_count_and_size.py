from akamai.netstorage import Netstorage, NetstorageError
import xml.etree.ElementTree as ET


NS_HOSTNAME = ''
NS_KEYNAME = ''
NS_KEY = ''
NS_CPCODE = ''

ns = Netstorage(NS_HOSTNAME, NS_KEYNAME, NS_KEY, ssl=False)
info = {}

def recursive(items):
	for item in items:
		if item.get('type') == 'file':
			k = items.attrib['directory'][7:]
			if k not in info.keys():
				info[k] = [1, int(item.get('size'))]
			else:
				info[k][0] += 1
				info[k][1] += int(item.get('size')) 	
		elif item.get('type') == 'dir':
			ok, res = ns.dir(items.attrib['directory'] + "/" + item.get('name'))
			if ok:
				xml_tree = ET.fromstring(res.content)
				try:
					recursive(xml_tree)
				except:
					pass

ok, res = ns.dir('/' + NS_CPCODE + '/path')

if ok:
	xml_tree = ET.fromstring(res.content)
	try:
		recursive(xml_tree)
		print(info)
	except Exception as e:
		print(e)
else:
	print('access deny')