def find_special_numbers():
    for number in range(100, 1000):
        digits = [int(d) for d in str(number)]
        product = digits[0] * digits[1] * digits[2]
        summation = sum(digits)
        if summation != 0 and product % summation == 0:
            print(number)
find_special_numbers()