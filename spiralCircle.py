# Let us create amazing spiral circle 
# The target of this code is knowing what hsv_to_rgb() do and mean it

# colorsys library give us the function hsv_to_rgb(h, s, v)

# This function convert hsv to rgb
# but what hsv mean?
# hsv aka ( Hue Saturation Value )
# it take values between 0 and 1 so you can pass float like 0.8

# fast example for your eyes🥰

from colorsys import hsv_to_rgb

# make unpack tuple to take r, g and b (red green blue)

h = 0.36
s = 0.62
v = 0.43
r, g, b = hsv_to_rgb(h, s, v)

# print the value r g b and see how the values will be different

print(f'h={h} s={s} v={v}\n')
print(f'r={r} g={g} b={b}')

"""
h=0.36 s=0.62 v=0.43

r=0.1634 g=0.43 b=0.20605600000000002
"""

# Now time of drawing🐱‍🏍🐱‍🏍

from turtle import *
from colorsys import hsv_to_rgb

bgcolor('black')
speed(0)

h, s, v = 0, 1, 1  # try change the values to understand
for i in range(50):
    h += 10/360
    color(hsv_to_rgb(h, s, v))
    circle(120)
    right(10)

mainloop()



