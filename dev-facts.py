from jnpr.junos.device import Device
from pprint import pprint

junos_hosts = ['192.168.122.92' ]
for ip in junos_hosts:
    dev = Device(host=ip, user='jcarranza', password='Junip3r', port=22)
    dev.open()
    pprint(dev.facts)

    dev.close()
