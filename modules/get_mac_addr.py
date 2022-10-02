
from scapy.all import *

def get_mac_addr(ip_addr):
	arp_packet = Ether()/ARP()
	arp_packet["ARP"].pdst = ip_addr
	arp_packet["Ethernet"].dst = "ff:ff:ff:ff:ff:ff" # broadcast MAC address
	res_packet = srp1(arp_packet, timeout=1, verbose=False)[0]
	return res_packet["ARP"].hwsrc