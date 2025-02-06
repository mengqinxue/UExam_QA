import re
import random
import inflect


def c56_generate_skip_counting_question():

    questions = []

    # step = 2
    step = 2
    start = random.randint(1, 20)
    sequence = [start + step * i for i in range(4)]
    correct = sequence[-1]  # 正确答案是第 4 个数

    # 生成干扰项，避免重复
    options = {correct}
    while len(options) < 4:
        distractor = correct + random.choice([-step, step, step * 2])
        options.add(distractor)

    options = list(options)
    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct)]

    question = [f"What comes next in the sequence? {sequence[0]}, {sequence[1]}, {sequence[2]}, ___",
            options[0], options[1], options[2], options[3], correct_option]

    questions.append(question)

    # step = 3
    start = random.randint(1, 20)
    step = 3
    sequence = [start + step * i for i in range(4)]
    correct = sequence[-1]  # 正确答案是第 4 个数

    # 生成干扰项，避免重复
    options = {correct}
    while len(options) < 4:
        distractor = correct + random.choice([-step, step, step * 3])
        options.add(distractor)

    options = list(options)
    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct)]

    question = [f"What comes next in the sequence? {sequence[0]}, {sequence[1]}, {sequence[2]}, ___",
                options[0], options[1], options[2], options[3], correct_option]

    questions.append(question)

    # step = 5
    start = random.randint(1, 20)
    step = 5
    sequence = [start + step * i for i in range(4)]
    correct = sequence[-1]  # 正确答案是第 4 个数

    # 生成干扰项，避免重复
    options = {correct}
    while len(options) < 4:
        distractor = correct + random.choice([-step, step, step * 5])
        options.add(distractor)

    options = list(options)
    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct)]

    question = [f"What comes next in the sequence? {sequence[0]}, {sequence[1]}, {sequence[2]}, ___",
                options[0], options[1], options[2], options[3], correct_option]

    questions.append(question)

    # step = 10
    start = random.randint(1, 20)
    step = 10
    sequence = [start + step * i for i in range(4)]
    correct = sequence[-1]  # 正确答案是第 4 个数

    # 生成干扰项，避免重复
    options = {correct}
    while len(options) < 4:
        distractor = correct + random.choice([-step, step, step * 10])
        options.add(distractor)

    options = list(options)
    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct)]

    question = [f"What comes next in the sequence? {sequence[0]}, {sequence[1]}, {sequence[2]}, ___",
                options[0], options[1], options[2], options[3], correct_option]

    questions.append(question)

    return questions


def c7_generate_skip_counting_puzzle():
    start = random.randint(10, 50)  # Starting number (realistic range)
    step = random.choice([2, 5, 10])  # Common skip-counting steps
    target = random.randint(start + step * 2, start + step * 10)  # Target within a range
    question_type = random.choice(["reach", "specific"])

    if question_type == "reach":
        question = f"Max skip-counted by {step}, beginning at {start}. Could he have said the number {target}?"
        correct_answer = "Yes" if (target - start) % step == 0 else "No"
    else:
        end = random.randint(start + 2, start + 10)  # A small end point
        question = f"Max skip-counted, starting at {start}, until he got to {end}. Could he be counted by {step}s?"
        correct_answer = "Yes" if (end - start) % step == 0 else "No"

    options = ["Yes", "No", "Maybe", "Not Sure"]
    random.shuffle(options)
    correct_option = "ABCD"[options.index(correct_answer)]

    res = [question, options[0], options[1], options[2], options[3], correct_option]

    return [res]


def c8_generate_year_three_question():
    # question_type = random.choice(["letter_position", "ordinal_number"])
    questions = []

    # "letter_position":
    passage = "What's in a name? That which we call a rose by any other name would smell as sweet."
    position = random.randint(1, len(passage.replace(" ", "")))  # Ignore spaces for counting
    filtered_passage = re.sub(r'\s+', '', passage)  # Remove spaces
    correct_answer = filtered_passage[position - 1]  # Find the character at that position

    options = list(set([correct_answer] + random.sample("abcdefghijklmnopqrstuvwxyz", 3)))
    random.shuffle(options)
    correct_option = "ABCD"[options.index(correct_answer)]

    question = f"What is the {position}-th letter in this passage? {passage}"

    questions.append([question, options[0], options[1], options[2], options[3], correct_option])

    # "ordinal_number"
    # words = ["Twenty-four", "47th", "Sixty-fifth", "Twenty-seven", "89th", "100th", "Thirty-three"]
    # correct_answer = random.choice(
    #     [w for w in words if not re.search(r'\d+(st|nd|rd|th)$', w)])  # Pick a non-ordinal number
    #
    # options = list(set([correct_answer] + random.sample(words, 3)))
    # random.shuffle(options)
    # correct_option = "ABCD"[options.index(correct_answer)]
    #
    # question = "Which of the following are ordinary numbers?"
    #
    # questions.append([question, options[0], options[1], options[2], options[3], correct_option])
    questions.append(["Which of the following are ordinary numbers?", "58", "sixity-one", "31st", "Million", "C"])

    return questions


def c9_generate_year_three_question():

    passage = "What's in a name? That which we call a rose by any other name would smell as sweet."
    position = random.randint(1, len(passage.replace(" ", "")))  # Ignore spaces for counting
    filtered_passage = re.sub(r'\s+', '', passage)  # Remove spaces
    correct_answer = filtered_passage[position - 1]  # Find the character at that position

    options = list(set([correct_answer] + random.sample("abcdefghijklmnopqrstuvwxyz", 3)))
    random.shuffle(options)
    correct_option = "ABCD"[options.index(correct_answer)]

    question = f"What is the {position}-th letter in this passage? {passage}"

    return [question, options[0], options[1], options[2], options[3], correct_option]


def c10_generate_question():

    questions = []

    # Thousands
    p = inflect.engine()
    num = random.randint(1000, 9999)  # Generate a random number between 1 and 9999
    num_in_words = p.number_to_words(num)

    correct_answer = p.number_to_words(num).replace(",", "").replace("-", " and")
    options = [
        correct_answer,
        p.number_to_words(num + random.choice([10, 20, 50, 100])).replace(",", "").replace("-", " and"),
        p.number_to_words(num - random.choice([10, 20, 50, 100])).replace(",", "").replace("-", " and"),
        p.number_to_words(num + random.choice([100, 200, 500])).replace(",", "").replace("-", " and")
    ]

    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct_answer)]

    questions.append([f"How do you write this number in words {num}?", options[0],
                      options[1], options[2], options[3], correct_option])

    # Million
    num = random.randint(1000000, 9990009)  # Generate a random number between 1 and 9999
    num_in_words = p.number_to_words(num)

    correct_answer = p.number_to_words(num).replace(",", "").replace("-", " and")
    options = [
        correct_answer,
        p.number_to_words(num + random.choice([10, 20, 50, 100])).replace(",", "").replace("-", " and"),
        p.number_to_words(num - random.choice([10, 20, 50, 100])).replace(",", "").replace("-", " and"),
        p.number_to_words(num + random.choice([100, 200, 500])).replace(",", "").replace("-", " and")
    ]

    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct_answer)]

    questions.append([f"How do you write this number in words {num}?", options[0],
                      options[1], options[2], options[3], correct_option])

    # Ordinal
    p = inflect.engine()
    num = random.randint(1, 100)  # Generate a random number between 1 and 9999
    correct_answer = p.ordinal(num)

    incorrect_answers = [
        p.ordinal(num + random.choice([1, 2, 3, 5])),
        p.ordinal(num - random.choice([1, 2, 3, 5])) if num > 1 else p.ordinal(num + 6),
        p.ordinal(num + random.choice([10, 20, 30])) if num <= 90 else p.ordinal(num - 10)
    ]

    options = [correct_answer] + incorrect_answers
    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct_answer)]

    questions.append([f"What is the ordinal form of {num}?", options[0],
                      options[1], options[2], options[3], correct_option])


    return  questions


def c11_generate_roman_numeral_question():
    roman_numerals = {
        1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
        20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
        100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
        1000: "M"
    }

    num = random.choice(list(roman_numerals.keys()))
    correct = roman_numerals[num]

    # 生成干扰项，确保不会重复
    options = {correct}
    while len(options) < 4:
        wrong_choice = random.choice(list(roman_numerals.values()))
        options.add(wrong_choice)

    options = list(options)
    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct)]
    return [f"What is {num} in Roman numerals?", options[0], options[1], options[2], options[3], correct_option]


def c12_compare():

    questions = []
    # ---------------------------------------------------------------
    # Generate two random numbers between 1 and 2000
    num1 = random.randint(1000, 9999)
    num2 = random.randint(1000, 9999)

    # Determine the correct comparison operator
    if num1 < num2:
        correct_answer = "<"
    elif num1 == num2:
        correct_answer = "="
    else:
        correct_answer = ">"

    # Generate the options by shuffling the correct and incorrect answers
    options = [correct_answer, "<", ">", "=", "not sure"]
    options = list(set(options))  # Remove duplicates (just in case)
    random.shuffle(options)  # Shuffle to randomize the positions of the options

    # Find the index of the correct option
    correct_option = "ABCD"[options.index(correct_answer)]

    # Return the question with options and the correct answer
    questions.append([f"Which of the following is the correct comparison: {num1} (?) {num2}?",
                      options[0], options[1], options[2], options[3], correct_option])

    # ---------------------------------------------------------------
    # Generate two random numbers between 1 and 2000
    num1 = random.randint(1000000, 9999999)
    num2 = random.randint(1000000, 9999999)

    # Determine the correct comparison operator
    if num1 < num2:
        correct_answer = "<"
    elif num1 == num2:
        correct_answer = "="
    else:
        correct_answer = ">"

    # Generate the options by shuffling the correct and incorrect answers
    options = [correct_answer, "<", ">", "=", "not sure"]
    options = list(set(options))  # Remove duplicates (just in case)
    random.shuffle(options)  # Shuffle to randomize the positions of the options

    # Find the index of the correct option
    correct_option = "ABCD"[options.index(correct_answer)]

    # Return the question with options and the correct answer
    questions.append([f"Which of the following is the correct comparison: {num1} (?) {num2}?",
                      options[0], options[1], options[2], options[3], correct_option])

    # ---------------------------------------------------------------
    # Generate two random numbers between 1 and 2000
    num1 = random.randint(1000, 9999)
    num2 = random.randint(1000, 9999)
    num3 = random.randint(1000, 9999)

    # Determine the correct comparison operator
    if num1 < num2:
        correct_answer = "<"
    elif num1 == num2:
        correct_answer = "="
    else:
        correct_answer = ">"

    # Generate the options by shuffling the correct and incorrect answers
    options = [correct_answer, "<", ">", "=", "not sure"]
    options = list(set(options))  # Remove duplicates (just in case)
    random.shuffle(options)  # Shuffle to randomize the positions of the options

    # Find the index of the correct option
    correct_option = "ABCD"[options.index(correct_answer)]

    # Return the question with options and the correct answer
    questions.append([f"Which of the following is the correct comparison: {num1 + num3} - {num3} (?) {num2}?",
                      options[0], options[1], options[2], options[3], correct_option])


    # ---------------------------------------------------------------
    # Generate two random numbers between 1 and 2000
    num1 = random.randint(1000, 9999)
    num2 = random.randint(1000, 9999)
    num3 = random.randint(1000, 9999)

    # Determine the correct comparison operator
    if num1 < num2:
        correct_answer = "<"
    elif num1 == num2:
        correct_answer = "="
    else:
        correct_answer = ">"

    # Generate the options by shuffling the correct and incorrect answers
    options = [correct_answer, "<", ">", "=", "not sure"]
    options = list(set(options))  # Remove duplicates (just in case)
    random.shuffle(options)  # Shuffle to randomize the positions of the options

    # Find the index of the correct option
    correct_option = "ABCD"[options.index(correct_answer)]

    # Return the question with options and the correct answer
    if num1 > num3:
        questions.append([f"Which of the following is the correct comparison: {num1 - num3} + {num3} (?) {num2}?",
                          options[0], options[1], options[2], options[3], correct_option])
    else:
        questions.append([f"Which of the following is the correct comparison: {num3 - num1} + {num3} (?) {num2}?",
                          options[0], options[1], options[2], options[3], correct_option])

    return questions


def main():
    print(c12_compare())

if __name__ == "__main__":
    main()