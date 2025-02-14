import random
def number_generation(num_numbers, num_digits, num_decimals):
    if not (len(num_digits) == len(num_decimals) == num_numbers):
        raise ValueError("The length of num_digits and num_decimals must match num_numbers.")

    numbers = []
    for i in range(num_numbers):
        if num_decimals[i] == 0:
            # Generate an integer
            num = random.randint(10 ** (num_digits[i] - 1), 10 ** num_digits[i] - 1)
        else:
            # Generate a float
            num = round(random.uniform(10 ** (num_digits[i] - 1), 10 ** num_digits[i] - 1), num_decimals[i])
        numbers.append(num)

    return numbers