# import turtle
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(10)
# turtle.pencolor("red")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.circle(40, 80/2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40*2/3)

import turtle
# 绘制坐标体系以及画笔的颜色和尺寸
def draw_pen(width, height, startX, startY, pen_size):
    turtle.setup(width, height, startX, startY)
    turtle.penup()
    turtle.pendown()
    turtle.pensize(pen_size)
    turtle.pencolor("red")
# turtle的运动轨迹
def turtle_Move(radius):
    turtle.circle(radius, None)
    turtle.circle(radius*(-1), None)
    turtle.seth(90)
    turtle.circle(radius, None)
    turtle.circle(radius * (-1), None)
    turtle.penup()
    turtle.fd(radius*2)
    turtle.pendown()
    turtle.seth(0)
    turtle.circle(radius*(-2), None)
    turtle.fd(radius*2)

    for i in range(4):
        if i != 0:
            turtle.seth(90*i*(-1))
            turtle.fd(radius*4)

    turtle.seth(0)
    turtle.fd(radius * 2)
draw_pen(0.5, 0.5, 200, 200, 10)
turtle_Move(80)
