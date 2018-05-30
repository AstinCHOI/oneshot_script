from akamai.netstorage import Netstorage, NetstorageError
import xml.etree.ElementTree as ET


NS_HOSTNAME = 'samsung_flagship_image_imc_eu-nsu.akamaihd.net'
NS_KEYNAME = 'jamespark_IMC_EU'
NS_KEY = 'lP1WSEN2C6xUg64u0aifgWtxrIqdU60WB4X6ff0l5fo2qq8x4t'
NS_CPCODE = '606569'


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

ok, res = ns.dir('/' + NS_CPCODE + '/uk/galaxy-note8/accessories')

if ok:
	xml_tree = ET.fromstring(res.content)
	try:
		recursive(xml_tree)
		print(info)
	except Exception as e:
		print(e)
else:
	print('access deny')