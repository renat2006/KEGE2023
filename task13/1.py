from ipaddress import *

net = ip_network(f"192.168.134.64/255.255.255.192", 0)

k = 0
for ip in net:
    k += 1
    s = str(ip).split(".")
    print(k, ip, s, ip.__str__().split("."))
