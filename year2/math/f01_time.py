import random
import turtle as ttt
from PIL import Image

class ClockGenerator():

    def __init__(self, filename):
        self.filename = filename
        self.t = ttt.Turtle()
        self.t.hideturtle()
        self.s = ttt.Turtle()
        self.s.hideturtle()
        self.s.left(90)
        self.s.speed(0)
        self.f = ttt.Turtle()
        self.f.hideturtle()
        self.f.left(90)
        self.f.speed(0)
        self.m = ttt.Turtle()
        self.m.hideturtle()
        self.m.left(90)
        self.m.speed(0)
        self.correct_time = self.generate_random_time()
        self.options = self.generate_options()
        self.draw_clock()
        self.draw_time()
        self.display_options()
        self.save_image()

    def generate_random_time(self):
        hh = random.randint(1, 12)  # 生成 1 到 12 之间的随机小时
        mm = random.randint(0, 59)  # 生成 0 到 59 之间的随机分钟
        return hh, mm

    def generate_options(self):
        options = [self.correct_time]
        while len(options) < 4:
            hh = random.randint(1, 12)
            mm = random.randint(0, 59)
            if (hh, mm) not in options:
                options.append((hh, mm))
        random.shuffle(options)
        return options

    def draw_clock(self):
        ttt.tracer(0)
        self.t.penup()
        self.t.seth(90)
        for i in range(12):
            self.t.right(360 / 12)
            self.t.forward(200)
            self.t.pendown()
            self.t.write(i + 1, align="center", font=("微软雅黑", 22, 'normal'))
            self.t.penup()
            self.t.backward(200)
        self.t.goto(220, 12)
        self.t.pendown()
        self.t.circle(220)  # 绘制半径为200的圆
        self.t.penup()
        ttt.update()

    def draw_time(self):
        hh, mm = self.correct_time

        self.s.clear()
        self.s.seth(90)
        self.s.right((hh + (mm / 60)) * 30)
        self.s.pensize(15)
        self.s.fd(60)
        self.s.fd(-60)
        ttt.update()

        self.f.clear()
        self.f.seth(90)
        self.f.right(mm * 6)
        self.f.pensize(7)
        self.f.fd(100)
        self.f.fd(-100)
        ttt.update()

    def display_options(self):
        question = []
        question.append("Please select right time: ")
        for i, option in enumerate(self.options):
            hh, mm = option
            question.append(f"{hh:02}:{mm:02}")
        correct_answer = self.options.index(self.correct_time) + 1
        correct_answer = chr(correct_answer + 64)
        question.append(correct_answer)
        # print(question)
        return question


    def save_image(self):
        # 获取底层的 Tkinter 画布
        canvas = ttt.getcanvas()
        # 保存为 PS 文件
        ps_file = "../../tmp/clock.ps"
        canvas.postscript(file=ps_file)
        # print(f"PostScript 文件已保存到: {ps_file}")

        # 将 PS 文件转换为 PNG 文件（需要安装 Pillow 库）
        png_file = self.filename
        img = Image.open(ps_file)
        img.save(png_file, "png")
        # print(f"PNG 文件已保存到: {png_file}")


cg = ClockGenerator(filename='../../tmp/clock.png')
cg.display_options()