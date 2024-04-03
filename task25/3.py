def simpl(a):
    for j in range(2, int(a ** 0.5) + 1):
        if a % j == 0:
            return False
    return True


for i in range(3175777, 3175811 + 1):
    if simpl(i):
        print(i, end=" ")
