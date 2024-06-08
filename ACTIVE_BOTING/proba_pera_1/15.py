for A in range(1,10000000):
    for x in range(1, 1000000):
        f =  ((x % A != 0) and (x % 35 == 0)) <= ((x % 21 != 0) or (x % 35 != 0))
        if f is False:
            break
    else:
        print(A)




