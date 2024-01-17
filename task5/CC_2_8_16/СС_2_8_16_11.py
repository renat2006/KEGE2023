count = 0

for N in range(1000, 5001):
    bin_n = bin(N)[2:]
    even_ones = 0
    odd_zeros = 0

    for i in range(len(bin_n)):
        if (i + 1) % 2 == 0:
            if bin_n[i] == '1':
                even_ones += 1
        else:
            if bin_n[i] == '0':
                odd_zeros += 1

    result = abs(even_ones - odd_zeros)

    if result >= 5:
        count += 1

print(count)
