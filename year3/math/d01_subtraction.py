import re
import random


def add_zero_after_numbers(s):
    # 定义正则表达式模式，匹配一个或多个数字
    pattern = r'\d+'
    # 使用 re.sub() 函数替换匹配到的数字，在后面添加 0
    result = re.sub(pattern, lambda m: m.group(0) + '0', s)
    return result


def generate_fruit_question(str):

    pattern = r'\d+'
    numbers = re.findall(pattern, str)

    object_list = ["apples", "oranges", "eggs", "bananas", "grapes", "pears"]
    selected_objects = random.sample(object_list, 2)

    question = f"I have {numbers[0]} {selected_objects[0]} and {numbers[1]} {selected_objects[1]}. How many objects do I have?"
    return question


def d01_generate_subtraction_problems(num_addends, integer_digits, decimal_digits):
    if len(integer_digits) != num_addends or len(decimal_digits) != num_addends:
        raise ValueError("integer_digits 和 decimal_digits 列表的长度必须等于 num_addends")

    addends = []
    for i in range(num_addends):
        num = round(random.uniform(10 ** (integer_digits[i] - 1), 10 ** integer_digits[i] - 1), decimal_digits[i])
        if decimal_digits[i] == 0:
            num = int(num)  # 去掉小数部分
        addends.append(num)

    # 确保第一个数是最大的，以避免结果为负数
    first_addend = max(addends)
    addends.remove(first_addend)
    addends.insert(0, first_addend)

    correct_answer = first_addend - sum(addends[1:])
    problem = " - ".join(map(str, addends)) + " = ?"

    # 生成三个错误的答案
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = round(random.uniform(correct_answer - 10, correct_answer + 10), max(decimal_digits))
        if decimal_digits[i] == 0:
            wrong_answer = int(wrong_answer)  # 去掉小数部分
        if wrong_answer != correct_answer and wrong_answer > 0:
            wrong_answers.add(wrong_answer)

    # 将正确答案和错误答案合并并打乱顺序
    options = list(wrong_answers) + [correct_answer]
    random.shuffle(options)

    question = [problem, options[0], options[1], options[2], options[3],
                "ABCD"[options.index(correct_answer)]]

    return question


def d09_d10_generate_math_question():
    # 随机生成两个数字
    base_number = random.randint(1, 100)
    correct_answer = random.randint(1, base_number)  # 确保结果不为负数

    target_number = base_number - correct_answer

    # 生成三个错误的答案
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = random.randint(target_number - 20, target_number + 20)
        if wrong_answer != correct_answer and wrong_answer > 0:
            wrong_answers.add(wrong_answer)

    # 将正确答案和错误答案合并并打乱顺序
    options = list(wrong_answers) + [correct_answer]
    random.shuffle(options)

    # 创建问题字符串
    problem = f"{base_number} - (?) = {target_number}"

    # 创建选项列表
    options_list = [f"{i}" for i in options]

    # 找到正确答案的索引
    correct_option_index = options.index(correct_answer)
    correct_option_letter = "ABCD"[correct_option_index]

    return [problem, options_list[0], options_list[1], options_list[2], options_list[3],
            correct_option_letter]



def d11_generate_math_question():
    # 生成题目中的数字
    num1 = random.randint(9, 20)
    num2 = random.randint(9, 20)
    num3 = random.randint(1, num1)  # 确保 num1 - num3 >= 0

    # 计算正确答案
    correct_answer = num1 - num3

    # 生成三个错误答案
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = random.randint(1, 40)
        if wrong_answer != correct_answer:
            wrong_answers.add(wrong_answer)

    # 将正确答案加入错误答案集合中，然后打乱顺序
    options = list(wrong_answers) + [correct_answer]
    random.shuffle(options)

    # 找到正确答案的索引
    correct_option_index = "ABCD"[options.index(correct_answer)]

    # 构建题目字符串
    question = f"{num1} - (?) = {num2}"

    return [question, options[0], options[1], options[2], options[3], correct_option_index]


# C01 一位整数加法
print(d01_generate_subtraction_problems(2, [1, 1], [0, 0]))

# C02 - Add multiples of 10
new_question = d01_generate_subtraction_problems(2, [1, 1], [0, 0])

for i in range(len(new_question)):
    if isinstance(new_question[i], str):
        new_question[i] = add_zero_after_numbers(new_question[i])
    else:
        new_question[i] = new_question[i] * 10

print(new_question)

# C03/C04 - Add a two-digit and a one-digit number
print(d01_generate_subtraction_problems(2, [2, 1], [0, 0]))
#
# C05/C06 - Add a two-digit and a two-digit number
print(d01_generate_subtraction_problems(2, [2, 2], [0, 0]))

# C07 - Compensation add

# C08 - addition word problem (e.g. "I have 5 apples and 3 oranges. How many fruits do I have?")
new_question = d01_generate_subtraction_problems(2, [2, 2], [0, 0])
new_question[0] = generate_fruit_question(new_question[0])
print(new_question)

# C09/C10 Addition input/output tables - up to two digits
print(d09_d10_generate_math_question())

# C11 - Balance addition equations - up to two digits
print(d11_generate_math_question())

# C12/C13 - Add three or more numbers up to two digits each
print(d01_generate_subtraction_problems(3, [2, 1, 1], [0, 0, 0]))

# C14C20 - Add two numbers up to three digits
print(d01_generate_subtraction_problems(2, [3, 3], [0, 0]))

# C22 - Add three or more numbers up to three digits each
print(d01_generate_subtraction_problems(3, [3, 2, 1], [0, 0, 0]))

# C25 - Add two numbers up to four digits
print(d01_generate_subtraction_problems(2, [4, 3], [0, 0]))

# C30
print(d01_generate_subtraction_problems(4, [4, 3, 2, 1], [0, 0, 0, 0]))

# C31
print(d01_generate_subtraction_problems(4, [4, 3, 3, 2], [0, 0, 0, 0]))