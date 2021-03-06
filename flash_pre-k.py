#coding:utf-8

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

arg = ''
if (len(sys.argv) >= 2):
    arg = sys.argv[1]

shuffle = ''
if (len(sys.argv) >= 3):
    shuffle = sys.argv[2]

s = turtle.getscreen()
width = s.window_width()
height = s.window_height()

def waitDraw(size):
    w = width - 40

    t.speed(2)
    t.up()
    t.goto(0 - width / 2 + 20, 0 - height / 2 + 20)
    t.down()
    t.pensize(3)
    t.pencolor('black')
    t.fd(w)
    t.left(180)
    t.pencolor('green')
    t.fd(w)
    t.left(180)
    t.pencolor('red')
    t.fd(w)
    turtle.ht()


def writeTxt(size, txt):
    t.clear()
    left = 0 - width / 2 + 20
    top = 0 - size / 2
    t.up()
    t.goto(left, top)
    t.down()
    t.pencolor('red')
    t.write(txt, font=('Times New Roman', size, ''))
    turtle.ht()

writeTxt(100, "开始学单词...")
waitDraw(500)
t.reset()

# lstAll = list(range(97, 123))
if ((shuffle == '--shuffle') or (shuffle == '-S')):
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
