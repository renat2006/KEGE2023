def generate_number(N):
    binary_N = bin(N)[2:]

    if N % 2 == 1:
        result_binary = '10' + binary_N + '11'
    else:
        result_binary = '1' + binary_N + '00'

    result_decimal = int(result_binary, 2)

    return result_decimal


min_result = 12000
for N in range(1, 1280):
    result = generate_number(N)
    if 1023 < result and result < min_result:
        min_result = result

print(min_result)
