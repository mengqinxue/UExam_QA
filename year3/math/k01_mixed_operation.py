import random

from common import numbers
from common import multi_choice


def k01_k02_generate_math_question(num_numbers, operators, num_digits, num_decimals):
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

    # Randomly choose operators
    question_operators = operators

    # Construct the question string
    question = str(numbers[0])
    for i in range(1, num_numbers):
        question += f" {question_operators[i - 1]} {numbers[i]}"

    # Calculate the correct answer
    correct_answer = eval(question)
    question = question + " = (?)"

    options, correct_answer_index = multi_choice.generate_options(correct_answer)

    return question, options[0], options[1], options[2], options[3], correct_answer_index


def k03_generate_math_question(type=1, num_digits=None, num_decimals=None):

    if num_digits is None:
        num_digits = [1, 1]
    if len(num_digits) != len(num_decimals):
        raise ValueError("The length of operators, num_digits, and num_decimals must match.")

    # Type 1: Addition vs. Subtraction
    if type == 1:
        number_list = numbers.number_generation(3, num_digits, num_decimals)
        number_list.sort(reverse=True)
        correct_value = number_list[0] + number_list[1] + number_list[2]
        question = f"{number_list[0]} + {number_list[1]} = (?) - {number_list[2]}"
        options, correct_answer_index = multi_choice.generate_options(correct_value)
        return question, options[0], options[1], options[2], options[3], correct_answer_index

    # Type 2: Subtraction vs. Addition
    elif type == 2:
        correct_value = 0
        while correct_value < 1:
            number_list = numbers.number_generation(3, num_digits, num_decimals)
            number_list.sort(reverse=True)
            correct_value = number_list[0] - number_list[2] - number_list[1]
            question = f"{number_list[0]} - {number_list[2]} = (?) + {number_list[1]}"
            options, correct_answer_index = multi_choice.generate_options(correct_value)
        return question, options[0], options[1], options[2], options[3], correct_answer_index

    # Type 3: Multiplication vs. Addition
    elif type == 3:
        number_list = numbers.number_generation(3, num_digits, num_decimals)
        number_list.sort(reverse=True)
        correct_value = number_list[0] * number_list[1] - number_list[2]
        question = f"{number_list[0]} * {number_list[1]} = (?) + {number_list[2]}"
        options, correct_answer_index = multi_choice.generate_options(correct_value)
        return question, options[0], options[1], options[2], options[3], correct_answer_index

    # Type 4: Multiplication vs. Subtraction
    elif type == 4:
        number_list = numbers.number_generation(3, num_digits, num_decimals)
        number_list.sort(reverse=True)
        correct_value = number_list[0] * number_list[1] + number_list[2]
        question = f"{number_list[0]} * {number_list[1]} = (?) - {number_list[2]}"
        options, correct_answer_index = multi_choice.generate_options(correct_value)
        return question, options[0], options[1], options[2], options[3], correct_answer_index

    # Type 5: Division vs. Addition
    elif type == 5:
        number_list = numbers.number_generation(3, num_digits, num_decimals)
        number_list.sort(reverse=True)
        correct_value = number_list[0] - number_list[2]
        question = f"{number_list[0] * number_list[1]} / {number_list[1]} = (?) + {number_list[2]}"
        options, correct_answer_index = multi_choice.generate_options(correct_value)
        return question, options[0], options[1], options[2], options[3], correct_answer_index

    # Type 6: Division vs. Subtraction
    elif type == 6:
        number_list = numbers.number_generation(3, num_digits, num_decimals)
        number_list.sort(reverse=True)
        correct_value = number_list[0] + number_list[2]
        question = f"{number_list[0] * number_list[1]} / {number_list[1]} = (?) - {number_list[2]}"
        options, correct_answer_index = multi_choice.generate_options(correct_value)
        return question, options[0], options[1], options[2], options[3], correct_answer_index

    # Type 7: Division vs. Multiplication
    elif type == 7:
        number_list = numbers.number_generation(3, num_digits, num_decimals)
        number_list.sort(reverse=True)
        correct_value = number_list[0]
        question = f"{number_list[0] * number_list[1] * number_list[2] } / {number_list[1]} = (?) * {number_list[2]}"
        options, correct_answer_index = multi_choice.generate_options(correct_value)
        return question, options[0], options[1], options[2], options[3], correct_answer_index

    return 0


def k04_generate_math_question(num_numbers, operators, num_digits, num_decimals, flag=True):
    if not (len(num_digits) == len(num_decimals) == num_numbers):
        raise ValueError("The length of num_digits and num_decimals must match num_numbers.")

    number_list = numbers.number_generation(num_numbers, num_digits, num_decimals)

    # Randomly choose operators
    question_operators = operators

    # Construct the question string
    question = str(number_list[0])
    for i in range(1, num_numbers):
        question += f" {question_operators[i - 1]} {number_list[i]}"

    # Calculate the correct answer
    if flag:
        correct_answer_value = eval(question)
        correct_answer = 'True'
    else:
        correct_answer_value = eval(question) + random.randint(-5, 5)
        correct_answer = 'False'

    question = question + f" = {correct_answer_value}"

    options, correct_answer_index = multi_choice.generate_options_true_false(correct_answer)

    return question, options[0], options[1], options[2], options[3], correct_answer_index



# Example usage:
question = k01_k02_generate_math_question(3, ['+', '-'], [1, 1, 1], [0, 0, 0])
print(question)

# k3
question = k03_generate_math_question(1, [2, 1, 1], [0, 0, 0])
print(question)

# k4
question = k04_generate_math_question(3, ['*', '-'], [1, 1, 1], [0, 0, 0],
                                      flag=True)
print(question)

# k5
question = k03_generate_math_question(2, [1, 1, 1], [0, 0, 0])
print(question)

question = k03_generate_math_question(3, [1, 1, 1], [0, 0, 0])
print(question)

question = k03_generate_math_question(4, [1, 1, 1], [0, 0, 0])
print(question)

question = k03_generate_math_question(5, [1, 1, 1], [0, 0, 0])
print(question)

question = k03_generate_math_question(6, [1, 1, 1], [0, 0, 0])
print(question)

question = k03_generate_math_question(7, [1, 1, 1], [0, 0, 0])
print(question)