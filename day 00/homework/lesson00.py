from turtle import *


#we want to paint house
#step one:  draw a square
speed(5)
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawning door
fillcolor()
forward(70)
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#making window
penup()
goto(0,0)
right(150)
forward(140)
right(90)
forward(20)
pendown()
color("blue")
begin_fill()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()
left(90)
penup()
forward(120)
pendown()
begin_fill()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()




exitonclick() 