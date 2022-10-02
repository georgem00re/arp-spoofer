
from modules.get_mac_addr import *

def restore_arp_cache(target_ip_addr, spoofed_ip_addr):

	arp_packet = ARP()
	arp_packet["ARP"].pdst = target_ip_addr # set destination IP address of ARP packet
	arp_packet["ARP"].hwdst = get_mac_addr(target_ip_addr) # set destination MAC address of ARP packet
	arp_packet["ARP"].hwsrc = get_mac_addr(spoofed_ip_addr) # set MAC address of ARP cache entry
	arp_packet["ARP"].psrc = spoofed_ip_addr # set IP address of ARP cache entry
	arp_packet["ARP"].op = "is-at" # set operation code of ARP packet. 2 = ARP Reply
	send(arp_packet, verbose = False) # send ARP packet
