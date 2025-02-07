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


print(b01_generate_cubes())
