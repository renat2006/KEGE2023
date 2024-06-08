f = open("load.txt")
K = int(f.readline())
N = int(f.readline())
a = []
last = 0
for i in range(N):
    st, end = map(int, f.readline().split())
    a.append([st, end])
a.sort()
cam = [0] * N
c = 0
for i in range(N):
    st, end = a[i]
    for j in range(K):
        if cam[j] < st:
            cam[j] = end
            last = j + 1
            c += 1
            break
print(c, last)

