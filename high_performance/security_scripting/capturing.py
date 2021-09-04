from scapy.all import *

frame = Ether(dst="15:16:89:fa:dd:09")/IP(dst="9.16.5.4")/TCP()/"this is my payload"

print(fram)

sendp(frame)