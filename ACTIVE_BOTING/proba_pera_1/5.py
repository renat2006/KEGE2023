for n in range(1, 1000000):
    n1 = bin(n)[2:]
    if n % 3 == 0:
        n2 = n1 + n1[-3:]
    else:
        n2 = n1 + bin((n % 3) * 3)[2:]
    n3 = int(n2, 2)
    if n3 < 76:
        print(n)
       
