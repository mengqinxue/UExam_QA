import random


def generate_options(correct_answer, num_options=4):
    options = [correct_answer]
    is_integer = isinstance(correct_answer, int)
    decimal_places = 0 if is_integer else len(str(correct_answer).split('.')[1])

    while len(options) < num_options:
        if is_integer:
            # Generate a random wrong integer answer
            wrong_answer = random.randint(correct_answer - 5, correct_answer + 5)
        else:
            # Generate a random wrong float answer with the same number of decimal places
            wrong_answer = round(random.uniform(correct_answer - 5, correct_answer + 5), decimal_places)

        if (wrong_answer not in options) & (wrong_answer > 0):
            options.append(wrong_answer)

    # Shuffle the options to randomize the order
    random.shuffle(options)

    # Find the index of the correct answer
    correct_index = 'ABCD'[options.index(correct_answer)]

    return options, correct_index


def generate_options_true_false(correct_answer, num_options=4):
    options = ['True', 'False', 'Either', 'Neither']

    # Shuffle the options to randomize the order
    random.shuffle(options)

    # Find the index of the correct answer
    correct_index = 'ABCD'[options.index(correct_answer)]

    return options, correct_index


def generate_options_compare(correct_answer, num_options=4):
    options = ['>', '<', '=', 'Not sure']

    # Shuffle the options to randomize the order
    random.shuffle(options)

    # Find the index of the correct answer
    correct_index = 'ABCD'[options.index(correct_answer)]

    return options, correct_index


# Example usage:
# print(generate_options(10, 4))  # Correct answer is an integer
# print(generate_options(10.5, 4))  # Correct answer is a float
