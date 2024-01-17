def transform_number(n):
    binary_n = f'{n:b}'
    print(binary_n)
    count_ones = binary_n.count('1')

    if count_ones % 2 == 0:

        binary_n = binary_n[binary_n.find("1") + 1:].lstrip('0')

    else:

        binary_n = binary_n.replace('0', '') + '1'
    count_ones = binary_n.count('1')
    if count_ones % 2 == 0:

        binary_n = binary_n[binary_n.find("1") + 1:].lstrip('0')

    else:

        binary_n = binary_n.replace('0', '') + '1'

    return int(binary_n, 2) if binary_n else 0


count = sum(1 for i in range(1, 1001) if transform_number(i) == 7)
print(count)