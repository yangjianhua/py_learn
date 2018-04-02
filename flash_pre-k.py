import turtle
import random
import time
import sys

# Get Words from http://www.sightwords.com/sight-words/dolch/
# "Pre-K Dolch Sight Words"

lstAll = ['a', 'and', 'away', 'big', 'blue', 'can', 'come',
    'down', 'find', 'for', 'funny', 'go', 'help', 'here', 'I',
    'in', 'is', 'it', 'jump', 'little', 'look', 'make', 'me',
    'my', 'not', 'one', 'play', 'red', 'run', 'said', 'see',
    'the', 'three', 'to', 'two', 'up', 'we', 'where', 'yellow', 'you']

t = turtle.Turtle()
if (len(sys.argv) >= 2):
    arg = sys.argv[1]
else:
    arg = ''

s = turtle.getscreen()
width = s.window_width()
height = s.window_height()

def waitDraw(size):
    w = width - 20

    t.speed(2)
    t.up()
    t.goto(0 - width / 2, 0 - height / 2 + 20)
    t.down()
    t.pensize(3)
    t.pencolor('black')
    t.fd(w)
    t.left(180)
    t.pencolor('red')
    t.fd(w)


def writeTxt(size, txt):
    t.clear()
    left = 0 - width / 2 + 20
    top = 0 - size / 2
    t.up()
    t.goto(left, top)
    t.down()
    t.pencolor('red')
    t.write(txt, font=('Arial', size, ''))
    turtle.ht()

letter = ""

# lstAll = list(range(97, 123))
random.shuffle(lstAll)

for i, val in enumerate(lstAll):
    if ((arg == '--upper') or (arg == '-U')):
        letter = val.upper()
    else:
        letter = val
    writeTxt(200, letter)
    waitDraw(300)
    t.reset()

writeTxt(100, 'REST')
time.sleep(10)

# n_letter = random.randint(97, 123)
# letter = chr(n_letter)
# writeTxt(300, letter)
# waitDraw(300)
# t.reset()
