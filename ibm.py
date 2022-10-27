from turtle import *
color('#0e5df1')
pensize(4)
write('IBM', align="center", font=('Courier', 100, 'bold'))
penup()
setpos(-130, 110)
pendown()
color('white')
n = 110
for i in range(5):
    fd(300)
    n -= 12
    penup()
    setpos(-130, n)
    pendown()

penup()
setpos(-130, 48)
pendown()
fd(300)
mainloop()
