
from modules.man_in_the_middle import *

gateway_ip_addr = "192.168.0.1"
target_ip_addr = "192.168.0.13" 

man_in_the_middle(target_ip_addr, gateway_ip_addr)