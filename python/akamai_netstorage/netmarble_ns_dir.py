
import json
import optparse
import os
import sys
import time
import xml.etree.ElementTree as ET

from akamai.netstorage import Netstorage, NetstorageError


JSON_FILE = 'nsAccounts.json'
LOG_DIR = 'log/'
CPCODE_PATH_LEN = 7 # /123456

class NetstorageParser(optparse.OptionParser):
    def format_epilog(self, formatter):
        return self.epilog


def _netstorageDir(node, directory, options, destTime, f=None):
    path = "{0}/{1}".format(directory[CPCODE_PATH_LEN:], node.get('name'))
    isDir = (node.get('type') == 'dir')

    if isDir:
        if options.folder:
            if options.output:
                f.write("{0}{1}\n".format(options.url, path))
            else:
                print("{0}{1}".format(options.url, path))

        ok, res = ns.dir(directory + "/" + node.get('name'))
        if ok:
            xml_tree = ET.fromstring(res.text)
            try:
                netstorageDir(xml_tree, options, destTime, f)
            except NetstorageError as ne:
                print("Netstorage Error: {0}".format(ne))
            except Exception as e:
                print("Error: {0}".format(e))
    else:
        if not options.folder:
            if options.output:
                f.write("{0}{1}\n".format(options.url, path))
            else:
                print("{0}{1}".format(options.url, path))


def netstorageDir(xml_tree, options, destTime, f=None):    
    for node in xml_tree:
        if destTime:
            if int(node.get('mtime')) >= destTime:
                _netstorageDir(node, xml_tree.attrib['directory'], options, destTime, f)
        else:
            _netstorageDir(node, xml_tree.attrib['directory'], options, destTime, f)


if __name__ == '__main__':
    with open(JSON_FILE) as f:
        data = json.load(f)

    usage = ''
    epilog = ''
    parser = NetstorageParser(usage=usage, epilog=epilog)

    parser.add_option('-a', '--alias',
        dest='alias',
        help='Netstorage API Alias. It uses {0} file'.format(JSON_FILE)
    )
    parser.add_option('-D', '--day', 
        dest='day',
        help='Latest files in the specific days'
    )
    parser.add_option('-H', '--hour',
        dest='hour',
        help='Latest files in the specific hours'
    )
    parser.add_option('-u', '--url', 
        dest='url', default='',
        help='http(s)://www.hostname - without path'
    )
    parser.add_option('-p', '--path', 
        dest='path', 
        help='Netstorage path except CP Code'
    )
    parser.add_option('-f', '--folder', 
        action='store_true', dest='folder', default=False, 
        help='See directory(folder) only'
    )
    parser.add_option('-o', '--output', 
        action='store_true', dest='output', default=False,
        help='Save to file'
    )
    

    (options, args) = parser.parse_args()
    nsInfo = data[options.alias]
    ns = Netstorage(
        nsInfo['hostname'],
        nsInfo['keyname'],
        nsInfo['key']
    )

    path = options.path
    if path:
        if path == '/':
            path == ''
        elif not path.startswith('/'):
            path = '/' + path

        if path.endswith('/'):
            path = path[:-1]
    else:
        path = ''

    path = '/{0}{1}'.format(nsInfo['cpcode'], path)
    ok, res = ns.dir(path)

    if ok:
        xml_tree = ET.fromstring(res.text)
        try:
            try:
                currentTime = int(time.time())
                destTime = 0
                f = None
                filename = ''
                timeopt = ''
                if options.hour:
                    destTime = currentTime - (int(options.hour) * 60 * 60)
                    timeopt = '_h' + options.hour
                elif options.day:
                    destTime = currentTime - (int(options.day) * 24 * 60 * 60)
                    timeopt = '_d' + options.day

                if options.output:
                    filename = time.strftime('%Y%m%d%H%M%S', \
                        time.localtime(currentTime)) + timeopt + ".txt"

                    if not os.path.exists(LOG_DIR):
                        os.mkdir(LOG_DIR)

                    f = open(LOG_DIR + filename, 'w')

                netstorageDir(xml_tree, options, destTime, f)
                if options.output:
                    print("==> {0} file created".format(filename))
            finally:
                if options.output and f:
                    f.close()
        except NetstorageError as ne:
            print("Netstorage Error: {0}".format(ne))
        except IOError as ie:
            print("IOError: {0}".format(ie))
        except Exception as e:
            print("Error: {0}".format(e))
    else:
        print("requested path: " + path)
        print("status code: {0}".format(res.status_code))
        print(res.text)