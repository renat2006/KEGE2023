with open("2.txt") as f:
    k = 0
    lines = f.readlines()
    for line in lines:
        l = line.strip()
        if l.count("S") == l.count("T"):
            k += 1
            print(l, l.count("S"), l.count("T"))
    print(k)
