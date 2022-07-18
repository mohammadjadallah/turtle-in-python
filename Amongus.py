# Draw Among us with python turtle
# pip install turtle

from turtle import *

#speed(0)
width(10)
up()
setpos(-100, -10)
down()

# draw body
# draw feet

def feet(a1,a2,s1,r1,r2):
    right(a1)
    forward(s1)
    circle(r1, r2)
    right(a2)
    forward(s1/4)

def headers():
# draw the thing between feet
    right(50)
    circle(60, -68)
    forward(-15)
    left(70)
    color('#81007f')
    forward(60)
    
    color('black')
    up()
    setpos(60, -5)
    setheading(90)
    down()

    # draw head
    fillcolor('#81007f')
    circle(80, 180)
    forward(5)

# draw the glass
def eyeglasses():
    right(100)
    circle(35, 200)
    right(10)
    forward(50)
    circle(35, 200)
    right(20)
    forward(45)

# draw the backpack
def backpack():
    for i in range(2):
        forward(30)
        left(90)
        forward(100)
        left(90)

# call all functions
if __name__ == '__main__':
    fillcolor('#81007f')
    begin_fill()
    feet(90,22,180,20,200)
    up()
    setpos(60, -10)
    down()
    feet(180,-22,180,-20,200)
    end_fill()

    begin_fill()
    headers()
    end_fill()
    up()
    setpos(15, 0)
    down()

    fillcolor('#9ecbdf')
    begin_fill()
    eyeglasses()
    end_fill()

    fillcolor('#81007f')
    begin_fill()
    up()
    goto(-105, -20)
    down()
    backpack()
    end_fill()

    mainloop()
