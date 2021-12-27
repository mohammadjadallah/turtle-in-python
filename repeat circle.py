# A lot of circles that create amazing shape

from turtle import *

Screen()
speed(0)

def frecCircle():
    color('blue')
    for i in range(150):
        circle(i * 2)
        left(8)

frecCircle()
mainloop()
