import ipaddress
k = 0
net = ipaddress.ip_network("106.184.0.0/255.248.0.0", 0)
for n in net:
    n1 = bin(int(n))[2:].zfill(32)
    if n1.count("1") % 2 != 0:
        k += 1
print(k)