import socket
from scapy.layers.inet import traceroute

addr = socket.gethostbyname('www.baidu.com')
target = [addr]
result, unans = traceroute(target,maxttl=10)
