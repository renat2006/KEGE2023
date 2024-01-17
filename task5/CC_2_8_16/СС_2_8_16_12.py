def generate_number(N):
    binary_N = bin(N)[2:]

    if N % 2 == 1:
        result_binary = '1' + binary_N + '11'
    else:
        result_binary = '11' + binary_N + '00'

    result_decimal = int(result_binary, 2)

    return result_decimal


max_result = 0
for N in range(1, 128):
    result = generate_number(N)
    if result < 127 and result > max_result:
        max_result = result

print(max_result)
