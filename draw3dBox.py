
import turtle

turtle.up()
turtle.setpos(50, -50)
turtle.down()
turtle.speed(0)

turtle.pensize(4)
turtle.fillcolor("green")

j = 4
turtle.begin_fill()
while j > 0: 
    for i in range(4):
        turtle.fd(100)
        turtle.left(90)
    turtle.left(90)
    j -= 1

# right 2d

turtle.fd(100)
turtle.seth(20)
turtle.fd(100)

turtle.fd(-100)
turtle.seth(90)
turtle.fd(100)
turtle.seth(20)
turtle.fd(100)

turtle.seth(-90)
turtle.fd(200)

turtle.seth(200)
turtle.fd(100)

turtle.back(100)
turtle.seth(90)

# surface

turtle.fd(203)
turtle.seth(180)

turtle.fd(200)

turtle.seth(-160)
turtle.fd(100)

turtle.end_fill()

turtle.hideturtle()
turtle.mainloop()

