import re
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches


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


def generate_circles_image(num_big_circles, num_small_circles_per_big_circle, filename):
    # 创建一个新的图形
    fig, ax = plt.subplots(figsize=(10, 10))

    # 设置背景颜色
    ax.set_facecolor('lightblue')

    # 大圆的半径
    big_circle_radius = 0.2

    # 小圆的半径
    small_circle_radius = 0.05

    # 计算大圆的中心位置
    num_cols = int(num_big_circles ** 0.5) + 1
    num_rows = int(num_big_circles / num_cols) + 1

    for i in range(num_big_circles):
        # 计算大圆的中心位置
        col = i % num_cols
        row = i // num_cols
        center_x = (col + 0.5) * 2 * big_circle_radius
        center_y = (row + 0.5) * 2 * big_circle_radius

        # 绘制大圆
        big_circle = patches.Circle((center_x, center_y), big_circle_radius, edgecolor='black', facecolor='white',
                                    linewidth=2)
        ax.add_patch(big_circle)

        # 计算小圆的位置
        angle_step = 2 * math.pi / num_small_circles_per_big_circle
        for j in range(num_small_circles_per_big_circle):
            angle = j * angle_step
            small_center_x = center_x + (big_circle_radius - small_circle_radius) * math.cos(angle)
            small_center_y = center_y + (big_circle_radius - small_circle_radius) * math.sin(angle)

            # 绘制小圆
            small_circle = patches.Circle((small_center_x, small_center_y), small_circle_radius, edgecolor='black',
                                          facecolor='red', linewidth=1)
            ax.add_patch(small_circle)

    # 设置坐标轴范围
    ax.set_xlim(0, num_cols * 2 * big_circle_radius)
    ax.set_ylim(0, num_rows * 2 * big_circle_radius)

    # 隐藏坐标轴
    ax.axis('off')

    # 显示图形
    plt.savefig("../../images/year3/math/" + filename)


def e01_understand_multiplication(num1, num2, filename='e1.jpg'):
    correct_answer = num1 * num2

    # generate three wrong answers
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = random.randint(1, 40)
        if wrong_answer != correct_answer:
            wrong_answers.add(wrong_answer)

    question = (f"The number of big circles is {num1} and the number of small circles is {num2}, "
                f"How many big circles are there?")

    options = list(wrong_answers) + [correct_answer]

    correct_option_index = "ABCD"[options.index(correct_answer)]

    generate_circles_image(num1, num2,  filename)

    return [question, options[0], options[1], options[2], options[3],correct_option_index]


def e01_generate_multiplication_problems(num_factors, integer_digits, decimal_digits):
    if len(integer_digits) != num_factors or len(decimal_digits) != num_factors:
        raise ValueError("integer_digits 和 decimal_digits 列表的长度必须等于 num_factors")

    factors = []
    for i in range(num_factors):
        num = round(random.uniform(10 ** (integer_digits[i] - 1), 10 ** integer_digits[i] - 1), decimal_digits[i])
        if decimal_digits[i] == 0:
            num = int(num)  # 去掉小数部分
        factors.append(num)

    correct_answer = 1
    for factor in factors:
        correct_answer *= factor
    problem = " * ".join(map(str, factors)) + " = ?"

    # 生成三个错误的答案
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = round(random.uniform(correct_answer - 100, correct_answer + 100), max(decimal_digits))
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


def e09_e10_generate_math_question():
    # 随机生成两个数字
    base_number = random.randint(1, 10)
    multiplier = random.randint(1, 10)
    correct_answer = base_number * multiplier

    # 生成三个错误的答案
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = random.randint(correct_answer - 20, correct_answer + 20)
        if wrong_answer != correct_answer:
            wrong_answers.add(wrong_answer)

    # 将正确答案和错误答案合并并打乱顺序
    options = list(wrong_answers) + [multiplier]
    random.shuffle(options)

    # 创建问题字符串
    problem = f"{base_number} × (?) = {correct_answer}"

    # 创建选项列表
    options_list = [f"{i}" for i in options]

    # 找到正确答案的索引
    correct_option_index = options.index(multiplier)
    correct_option_letter = "ABCD"[correct_option_index]

    return [problem, options_list[0], options_list[1], options_list[2], options_list[3],
            correct_option_letter]


def e11_generate_math_question():
    # 生成题目中的数字
    num1 = random.randint(2, 10)  # 乘法因子范围调整
    num2 = random.randint(2, 10)  # 乘法因子范围调整
    num3 = random.randint(1, num1 * num2 - 1)  # 确保 num1 * num2 > num3

    # 计算正确答案
    correct_answer = num1 * num2 - num3

    # 生成三个错误答案
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = random.randint(1, 100)  # 调整错误答案范围
        if wrong_answer != correct_answer:
            wrong_answers.add(wrong_answer)

    # 将正确答案加入错误答案集合中，然后打乱顺序
    options = list(wrong_answers) + [correct_answer]
    random.shuffle(options)

    # 找到正确答案的索引
    correct_option_index = "ABCD"[options.index(correct_answer)]

    # 构建题目字符串
    question = f"{num3} + (?) = {num1} × {num2}"

    return [question, options[0], options[1], options[2], options[3], correct_option_index]




#e01
print(e01_understand_multiplication(2, 3, filename='e1.jpg'))

print(e01_generate_multiplication_problems(2, [1, 1], [0, 0]))

print(e01_generate_multiplication_problems(2, [2, 1], [0, 0]))

print(e01_generate_multiplication_problems(3, [1, 1, 1], [0, 0, 0]))

print(e09_e10_generate_math_question())

print(e11_generate_math_question())