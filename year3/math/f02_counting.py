import re
import random


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


import random
import re


def c9_generate_year_three_question():
    question_type = random.choice(["letter_position", "ordinal_number"])

    if question_type == "letter_position":
        passage = "What's in a name? That which we call a rose by any other name would smell as sweet."
        position = random.randint(1, len(passage.replace(" ", "")))  # Ignore spaces for counting
        filtered_passage = re.sub(r'\s+', '', passage)  # Remove spaces
        correct_answer = filtered_passage[position - 1]  # Find the character at that position

        options = list(set([correct_answer] + random.sample("abcdefghijklmnopqrstuvwxyz", 3)))
        random.shuffle(options)
        correct_option = "ABCD"[options.index(correct_answer)]

        question = f"What is the {position}-th letter in this passage? {passage}"

    else:  # "ordinal_number"
        words = ["Twenty-four", "47th", "Sixty-fifth", "Twenty-seven", "89th", "100th", "Thirty-three"]
        correct_answer = random.choice(
            [w for w in words if not re.search(r'\d+(st|nd|rd|th)$', w)])  # Pick a non-ordinal number

        options = list(set([correct_answer] + random.sample(words, 3)))
        random.shuffle(options)
        correct_option = "ABCD"[options.index(correct_answer)]

        question = "Which of the following are ordinary numbers?"

    return [question, f"A) {options[0]}", f"B) {options[1]}", f"C) {options[2]}", f"D) {options[3]}", correct_option]



def main():
    print(c8_generate_year_three_question())

if __name__ == "__main__":
    main()