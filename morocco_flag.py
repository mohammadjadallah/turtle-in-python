from turtle import *

# Initialize the screen
screen = Screen()
# setup the screen
screen.setup(600, 450)
# Change the position of the cursor
setpos(-200, -100)
# change the pen size, color, speed, title
pensize(4)
fillcolor('red')
title("Morocco Flag")
# speed(0)
# Initial Variables
n1 = 450
n2 = 300
# Create a box of the flag
begin_fill()
for i in range(2):
    fd(n1)
    left(90)
    fd(n2)
    left(90)
end_fill()

# Change the position to the middle of the BOX
up(); setpos(-30, 30); down()
color('green')
# Coordinates of the star on the flag
seth_fd = [(60, 100), (-60, 100), (150, 120), (0, 110), (-150, 120)]
# Draw the star
for s, f in seth_fd:
    seth(s)
    fd(f)

# write text
up(); setpos(-65, -150); down()
write("Morocco Won", font="normal 20 bold")

# hide the turtle
hideturtle()
# static screen
done()

# Ready........................................................




