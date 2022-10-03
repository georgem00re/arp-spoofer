
import os

def enable_ip_forwarding():
	os.system('sysctl -w net.inet.ip.forwarding=1')
