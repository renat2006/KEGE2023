for n in range(1000000):
    s = ">" + 19 * "0" + n * "1" + 36 * "2"
    while ">1" in s or ">2" in s or ">0" in s:
        s = s.replace(">1", "23>", 1)
        s = s.replace(">2", "2>", 1)
        s = s.replace(">0", "3>", 1)
    s = s.replace(">", "")
    if sum(map(int, s)) % 27 == 0:
        print(n)
        break
