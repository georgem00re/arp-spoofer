
import os

def disable_ip_forwarding():
	os.system('sysctl -w net.inet.ip.forwarding=0')
