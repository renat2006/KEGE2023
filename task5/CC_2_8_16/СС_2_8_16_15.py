def transform_number(n):
    binary_n = f'{n:b}'

    count_ones = binary_n.count('1')

    if count_ones % 2 == 0:

        binary_n = binary_n[binary_n.find("1") + 1:].lstrip('0')

    else:

        binary_n = "1" + binary_n + '00'
    count_ones = binary_n.count('1')
    if count_ones % 2 == 0:

        binary_n = binary_n[binary_n.find("1") + 1:].lstrip('0')

    else:

        binary_n = "1" + binary_n + '00'

    return int(binary_n, 2) if binary_n else 0


for n in range(1, 10000):
    if transform_number(n) > 100:
        print(n)
        break