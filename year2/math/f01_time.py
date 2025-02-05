import turtle as ttt
import time

t = ttt.Turtle()
t.hideturtle()
s = ttt.Turtle()
s.hideturtle()
s.left(90)
s.speed(0)
f = ttt.Turtle()
f.hideturtle()
f.left(90)
f.speed(0)
m = ttt.Turtle()
m.hideturtle()
m.left(90)
m.speed(0)


def draw_table():
    ttt.tracer(0)
    t.penup()
    t.seth(90)
    for i in range(12):
        t.right(360 / 12)
        t.forward(200)
        t.pendown()
        t.write(i + 1, align="center", font=("微软雅黑", 18, 'normal'))
        t.penup()
        t.backward(200)
    ttt.update()


def draw_time():
    localtime = time.localtime(time.time())
    global __hh
    __hh = localtime[3] % 12
    global __ff
    __ff = localtime[4]
    global __mm
    __mm = localtime[5]
    print(__hh, __ff, __mm)

    s.clear()
    s.seth(90)
    s.right((__hh + (__ff / 60)) * 30)
    s.pensize(15)
    s.fd(60)
    s.fd(-60)
    ttt.update()

    f.clear()
    f.seth(90)
    f.right(__ff * 6)
    f.pensize(7)
    f.fd(100)
    f.fd(-100)
    ttt.update()

    m.clear()
    m.seth(90)
    m.right(__mm * 6)
    m.pensize(3)
    m.fd(170)
    m.fd(-170)
    ttt.update()


draw_table()

while True:
    time.sleep(0.99)
    draw_time()
    ttt.update()
