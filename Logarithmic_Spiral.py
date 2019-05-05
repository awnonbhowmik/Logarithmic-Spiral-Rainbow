
import turtle as ob
import math as m

ob.speed(1000)
ob.hideturtle
wn=ob.Screen()
wn.bgcolor("black")


def LogSpiral(a, b):
    ob.up()
    ob.setpos(0, 0)
    ob.down()

    cl_map=["violet","indigo","blue","green","yellow","orange","red"]
    c=0
    for i in range(0, 3000, 5):
      ob.pencolor(cl_map[c])
      t = m.radians(i)
      x = a*m.exp(b*t)*m.cos(t)
      y = a*m.exp(b*t)*m.sin(t)
      ob.setpos(x, y)
      c=c+1
      c=c%7

LogSpiral(0.20, 0.20)