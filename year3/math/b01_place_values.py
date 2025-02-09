import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random

def generate_cuboid(x, y, z):
    """
    生成一个x*y*z的立方体结构，用1表示小立方体，用0表示空位。

    参数:
    x (int): 立方体的x轴长度
    y (int): 立方体的y轴长度
    z (int): 立方体的z轴长度

    返回:
    list: 三维列表表示的立方体结构
    """
    cuboid = [[[1 for _ in range(z)] for _ in range(y)] for _ in range(x)]
    return cuboid


def plot_cuboid(cuboid, filename):
    """
    绘制立方体结构。

    参数:
    cuboid (list): 三维列表表示的立方体结构
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 定义一个函数来绘制单个小立方体
    def draw_cube(x, y, z):
        r = [[x, y, z], [x, y, z+1], [x, y+1, z], [x, y+1, z+1],
             [x+1, y, z], [x+1, y, z+1], [x+1, y+1, z], [x+1, y+1, z+1]]
        faces = [[r[0], r[1], r[3], r[2]],
                 [r[4], r[5], r[7], r[6]],
                 [r[0], r[1], r[5], r[4]],
                 [r[2], r[3], r[7], r[6]],
                 [r[0], r[2], r[6], r[4]],
                 [r[1], r[3], r[7], r[5]]]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='b', alpha=.25))

    # 遍历立方体结构并绘制每个小立方体
    for i in range(len(cuboid)):
        for j in range(len(cuboid[i])):
            for k in range(len(cuboid[i][j])):
                if cuboid[i][j][k] == 1:
                    draw_cube(i, j, k)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.savefig('../../images/year3/math/' + filename)


def b01_generate_cubes():
    # 随机生成 x, y, z 的值
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    z = random.randint(1, 9)

    # 示例：生成一个随机大小的立方体并打印
    cuboid = generate_cuboid(x, y, z)

    correct_answer = x*y*z
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong_answer = random.randint(1, 100)
        if wrong_answer != correct_answer:
            wrong_answers.add(wrong_answer)

    options = list(wrong_answers) + [correct_answer]
    random.shuffle(options)

    correct_option_index = options.index(correct_answer)
    correct_option = chr(65 + correct_option_index)

    plot_cuboid(cuboid, 'b1.jpg')

    return ['The number of cubes is ', options[0], options[1], options[2], options[3], correct_option]


def b02_generate_math_question():
    # 随机生成一个四位数
    number = random.randint(1000, 9999)
    number_str = str(number)

    # 随机选择一个数字作为问题中的目标数字
    target_digit = random.choice(number_str)

    # 定义选项
    options = ["ones place", "tens place", "hundreds place", "thousands place"]

    # 找到目标数字的位置
    position = len(number_str) - number_str.index(target_digit) - 1

    # 根据位置选择正确的选项
    correct_option = options[position]

    # 打乱选项顺序
    random.shuffle(options)

    correct_option = "ABCD"[options.index(correct_option)]

    # 生成问题和选项
    question = [f"Where is the digit {target_digit} in {number}?", options[0], options[1], options[2], options[3], correct_option]

    return question


def b03_generate_math_question():
    # 随机生成一个六位数
    number = random.randint(100000, 999999)
    number_str = str(number)

    # 定义位置和对应的选项
    positions = {
        "ones place": -1,
        "tens place": -2,
        "hundreds place": -3,
        "thousands place": -4,
        "ten-thousands place": -5,
        "hundred-thousands place": -6
    }

    # 随机选择一个位置
    selected_position = random.choice(list(positions.keys()))
    selected_digit = number_str[positions[selected_position]]

    # 生成选项，包括正确的选项和三个随机的其他数字
    options = [selected_digit]
    while len(options) < 4:
        random_digit = str(random.randint(0, 9))
        if random_digit not in options:
            options.append(random_digit)

    # 打乱选项顺序
    random.shuffle(options)

    correct_option = "ABCD"[options.index(selected_digit)]

    # 生成问题和选项
    question = [f"Which digit is in the {selected_position} in {number}?",
                options[0], options[1], options[2], options[3], correct_option]

    return question


def b15_generate_math_question():
    # 随机生成一个六位数
    number = random.randint(100000, 999999)
    number_str = str(number)

    # 定义位置和对应的数字
    positions = {
        "hundred-thousands place": number_str[0],
        "ten-thousands place": number_str[1],
        "thousands place": number_str[2],
        "hundreds place": number_str[3],
        "tens place": number_str[4],
        "ones place": number_str[5]
    }

    # 随机选择一个位置
    selected_position = random.choice(list(positions.keys()))
    selected_digit = positions[selected_position]

    # 生成描述
    description_parts = []
    for position, digit in positions.items():
        description_parts.append(f"{digit} in the {position}")

    description = ", ".join(description_parts[:-1]) + f", and {description_parts[-1]}"

    # 生成问题
    question = (f"We can now write the number by combining these digits. The number has {description}. "
                f"So the number is (?)")

    # 生成选项
    correct_option = number
    options = [correct_option]

    while len(options) < 4:
        random_number = random.randint(100000, 999999)
        if random_number not in options:
            options.append(random_number)

    # 打乱选项顺序
    random.shuffle(options)

    question = [question, options[0], options[1], options[2], options[3], "ABCD"[options.index(correct_option)]]

    return question




print(b15_generate_math_question())
