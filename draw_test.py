from random import randint, choice
from turtle import Turtle, Screen
import time

screen = Screen()
screen.tracer(0)

width, height = screen.window_width() - 30, screen.window_height() - 30  # -30 to account for window borders, etc.

maker1 = Turtle(visible=False)
maker2 = maker1.clone()
maker3 = maker1.clone()
maker4 = maker1.clone()

maker1.goto(50, 50)  # top right
maker2.goto(50, -50)  # bottom right
maker3.goto(-50, -50)  # bottom left
maker4.goto(-50, 50)  # top left

n = randint(1, 360)
m = randint(0, 100)
r = randint(0, 50)
d = choice([True, False])

def out_of_bounds(turtle):
    return not (-width//2 < turtle.xcor() < width//2 and -height//2 < turtle.ycor() < height//2)

while r < 50:
    for i in range(0, m):

        maker1.forward(m)
        maker2.forward(m)
        maker3.backward(m)
        maker4.backward(m)

        if any(out_of_bounds(turtle) for turtle in screen.turtles()):
            for turtle in screen.turtles():
                turtle.undo()

        if d:
            maker1.right(r * n)
            maker2.right(-r * n)
            maker3.left(-r * n)
            maker4.left(r * n)
        else:
            maker1.left(r * n)
            maker2.left(-r * n)
            maker3.right(-r * n)
            maker4.right(r * n)

        maker1.forward(m)
        maker2.forward(m)
        maker3.backward(m)
        maker4.backward(m)

        if any(out_of_bounds(turtle) for turtle in screen.turtles()):
            for turtle in screen.turtles():
                turtle.undo()

    r += 1
    n = randint(0, 359)

screen.update()
screen.exitonclick()

time.sleep(10)