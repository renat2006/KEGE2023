import ipaddress
net3 = ipaddress.ip_address(f"111.81.80.0")
print(bin(int(net3))[2:].zfill(32))

for mask in range(33):
    net1 = ipaddress.ip_network(f"111.81.93.127/{mask}", 0)
    net2 = ipaddress.ip_network(f"111.81.80.0/{mask}", 0)
    if net1 == net2 and net2[0] == net3:
        print(bin(int(net1[0]))[2:].zfill(32), bin(int(net2[0]))[2:].zfill(32))
        print(str(net1.netmask).split("."))