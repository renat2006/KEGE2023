def count_zeros_and_ones(binary_str):
    count_zeros = binary_str.count('0')
    count_ones = binary_str.count('1')
    return count_zeros, count_ones


def generate_new_number(N):
    binary_N = bin(N)[2:]

    for _ in range(3):
        count_zeros, count_ones = count_zeros_and_ones(binary_N)
        if count_zeros == count_ones:
            binary_N += binary_N[-1]
        elif count_zeros > count_ones:
            binary_N += '1'
        else:
            binary_N += '0'

    decimal_result = int(binary_N, 2)
    return decimal_result


N = 132
while True:
    result = generate_new_number(N)
    octal_result = oct(result)
    if octal_result.endswith('0'):
        print(N)

        break
    N += 1
