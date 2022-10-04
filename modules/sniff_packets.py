
from scapy.all import *

def sniff_packets(iface, filter):
	pckets = sniff(iface=iface, prn=lambda x:x.summary(), filter=filter)