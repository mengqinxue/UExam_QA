import random


def c1_generate_counting_even_odd_question():
    questions = []

    counts = [random.randint(1, 20) for _ in range(3)]  # Generate three random numbers
    total_count = sum(counts)

    lines = []
    for count in counts:
        line = "* " * count
        lines.append(line)

    result = '\n'.join(lines)

    correct = "Even" if total_count % 2 == 0 else "Odd"
    correct_option = "A" if correct == "Even" else "B"

    questions.append([f"Is the total number of stars Even or Odd? \n" + result, "Even", "Odd", "", "", correct_option])

    return questions


def c2_generate_even_odd_question():
    questions = []

    for _ in range(1):  # Generate two "classify" questions
        num = random.randint(1, 100)
        correct = "Odd" if num % 2 else "Even"
        correct_option = "A" if correct == "Even" else "B"
        questions.append([f"Is {num} even or odd?", "Even", "Odd", "", "", correct_option])

    for _ in range(1):  # Generate two "identify_odd" questions
        odd_num = random.choice([x for x in range(1, 100, 2)])
        even_numbers = random.sample([x for x in range(2, 100, 2)], 3)
        options = even_numbers + [odd_num]
        random.shuffle(options)
        correct_option = "ABCD"[options.index(odd_num)]
        questions.append(
            [f"Which of the following numbers is odd?", options[0], options[1], options[2], options[3], correct_option])

    for _ in range(1):  # Generate two "identify_even" questions
        even_num = random.choice([x for x in range(2, 100, 2)])
        odd_numbers = random.sample([x for x in range(1, 100, 2)], 3)
        options = odd_numbers + [even_num]
        random.shuffle(options)
        correct_option = "ABCD"[options.index(even_num)]
        questions.append([f"Which of the following numbers is even?", options[0], options[1], options[2], options[3],
                          correct_option])

    return questions


def c3_generate_even_odd_sequence_questions():
    questions = []

    # Type 1: Which even number comes before?
    even_num = random.choice(range(6, 50, 2))  # Select an even number greater than 4
    sequence = [even_num - 4, even_num - 2, even_num, even_num + 2]
    correct_option = "ABCD"[sequence.index(even_num - 2)]
    questions.append([
        f"Which even number comes before? (?), {sequence[1]}, {sequence[2]}, {sequence[3]}",
        sequence[0], sequence[1], sequence[2], sequence[3], correct_option
    ])

    # Type 2: Which odd number comes next?
    odd_num = random.choice(range(471, 499, 2))  # Select an odd number less than 500
    sequence = [odd_num - 4, odd_num - 2, odd_num, "?"]
    correct_option = "ABCD"[0]
    questions.append([
        f"Which odd number comes next? {sequence[0]}, {sequence[1]}, {sequence[2]}, {sequence[3]}",
        odd_num + 2, odd_num + 4, odd_num + 6, odd_num + 8, correct_option
    ])

    # Type 3: Which odd number comes right after?
    even_num = random.choice(range(10, 100, 2))  # Select an even number
    correct = even_num + 1  # The next odd number
    options = random.sample(range(1, 150, 2), 3) + [correct]
    random.shuffle(options)
    correct_option = "ABCD"[options.index(correct)]
    questions.append([
        f"Which odd number comes right after {even_num}?",
        options[0], options[1], options[2], options[3], correct_option
    ])

    return questions


def c4_generate_subtraction_even_odd_question():
    num1 = random.randint(10, 99)  # Generate a two-digit number
    num2 = random.randint(1, num1)  # Ensure num2 is smaller for non-negative result
    result = num1 - num2  # Compute subtraction result
    correct_answer = "Even" if result % 2 == 0 else "Odd"

    # Generate four options, including the correct answer
    options = ["Even", "Odd", "Neither", "Both"]
    random.shuffle(options)  # Shuffle to randomize positions

    correct_option = "ABCD"[options.index(correct_answer)]  # Get correct answer letter

    question = f"Is {num1} - {num2} even or odd?"
    return [[question, options[0], options[1], options[2], options[3], correct_option]]