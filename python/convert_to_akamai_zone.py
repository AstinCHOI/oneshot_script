import subprocess
import sys

fastdns = sys.argv[1] # ['a7-65.akam.net.','a1-86.akam.net.','a2-66.akam.net.','a14-65.akam.net.','a26-67.akam.net.','a5-64.akam.net.']
TLD = sys.argv[2] # 'xxxx.com'
zonefile = sys.argv[3] # 'xxxx.com.zone.txt'

if len(sys.argv) < 4:
    print("usage: convert_to_akamai_zone.py ADAMDNS.net TLD zonefile")
else:
    print("This needs to install 'dig' application.")
    print(""" === converting type ===
$TTL xxx
@       IN    SOA     xxx.net. dnsadmin.cdnetworks.com. (
      2018060702 ;serial number
      900 ;refresh timer
      900 ;retry time
      604800 ;expire timer
      86400 ;minimum timer
)
;NS
@     IN      NS      xxx.net.
@     IN      NS      xxx.net.
;MX
@     IN      MX      10    xxx.xxx.com.
;A
xxx     IN      A       165.141.113.91
@     IN      A       165.141.183.73
""")
    print("=================")

with open(zonefile) as f:
    RECORD = ''
    hostname = ''
    for i, line in enumerate(f):
        line = line.strip()
        if i > 15 and line:
            if line.startswith(';'):
                RECORD = line[1:]
                continue
            else:
                line = line.split()
                if line[0] == '@':
                    hostname = TLD
                else:
                    hostname = line[0] + "." + TLD
            cmd = []
            cmd.append("dig")
            cmd.append("+short")
            cmd.append(hostname)
            cmd.append(RECORD)
            cmd.append("@" + fastdns)

            output = subprocess.check_output(cmd)
            output = output.decode().strip()
            if RECORD == 'SRV':
                if ' '.join(line[3:]) == output:
                    pass
                else:
                    print(cmd)
                    print("expected: " + line[3])
                    print("your input: " + output)    
            elif  line[3] in output.split():
                pass
            else:
                print(cmd)
                print("expected: " + line[3])
                print("your input: " + output)