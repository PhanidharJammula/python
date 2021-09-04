from scapy.all import *

frame = Ether(dst="15:16:89:fa:dd:09")/IP(dst="192.168.0.160")/TCP()/"this is my payload"

print(frame)

sendp(frame)