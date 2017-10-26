import turtle
myturtle=turtle.Turtle()

def square(length):
  myturtle.forward(length)
  myturtle.right(90)
  myturtle.forward(length)
  myturtle.right(90)
  myturtle.forward(length)
  myturtle.right(90)
  myturtle.forward(length)


squareLen=int(input("enter length of square"))
gapAngle=int(input("enter gap angle b/w squares"))


for i in range(int(360/gapAngle)):
  square(squareLen)
  myturtle.right(90 + gapAngle)
