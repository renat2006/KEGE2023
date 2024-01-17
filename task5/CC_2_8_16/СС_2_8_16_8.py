def calculate_R(N):
    octal_N = oct(N)[2:]
    first_two_digits = octal_N[:2][::-1]
    octal_R = octal_N + first_two_digits
    decimal_R = int(octal_R, 8)
    return decimal_R


N = 1

while True:
    result = calculate_R(N)
    if result > 1000:
        print(N)
        break
    N += 1
