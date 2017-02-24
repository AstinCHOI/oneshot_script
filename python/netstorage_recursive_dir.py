from akamai.netstorage import Netstorage, NetstorageError
import xml.etree.ElementTree as ET


NS_HOSTNAME = 'hostname'
NS_KEYNAME = 'keyname'
NS_KEY = 'key'
NS_CPCODE = 'cpcode'

ns = Netstorage(NS_HOSTNAME, NS_KEYNAME, NS_KEY, ssl=False)

def recursive(items):
	for item in items:
		if item.get('type') == 'file':
			print("{0} {1}".format(
				item.get('md5'),
				items.attrib['directory'][7:] + "/" + item.get('name')
			))
			# print("{0} {1} {2} {3} {4}".format(
			# 	items.attrib['directory'] + "/" + item.get('name'),
			# 	item.get('size'),
			# 	item.get('md5'),
			# 	item.get('mtime'),
			# 	item.get('type')
			# ))
		elif item.get('type') == 'dir':
			# print("{0} {1} {2} {3} {4}".format(
			# 	items.attrib['directory'] + "/" + item.get('name'),
			# 	item.get('bytes'),
			# 	item.get('files'),
			# 	item.get('mtime'),
			# 	item.get('type')
			# ))
			ok, res = ns.dir(items.attrib['directory'] + "/" + item.get('name'))
			if ok:
				xml_tree = ET.fromstring(res.content)
				try:
					recursive(xml_tree)
				except:
					pass


ok, res = ns.dir('/' + NS_CPCODE)
if ok:
	xml_tree = ET.fromstring(res.content)
	try:
		recursive(xml_tree)
	except:
		pass
