import turtle as tu

roo = tu.Turtle()  # create object
wn = tu.Screen()  # screen object
wn.bgcolor("black")  # screen background
wn.title("分形树")
roo.left(90)  # move
roo.speed(20)  # speed


def draw(l):  # Recursive function with length 'l' as parameter
    if l < 10:
        return
    else:
        roo.pensize(2)  # Set brush size
        roo.pencolor("yellow")  # Brush color
        roo.forward(l)  # orientations
        roo.left(30)  # move
        draw(3 * l / 4)  # paint
        roo.right(60)  # move
        draw(3 * l / 4)  # paint
        roo.left(30)  # move
        roo.pensize(2)
        roo.backward(l)  # back to initial address


draw(20)  # print 20 times

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")  # magenta
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red")  # red
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)


########################################################

def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(3)
        roo.pencolor("lightgreen")  # lightgreen
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red")  # red
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow")  # yellow
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)


########################################################
def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("cyan")  # cyan
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")  # yellow
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")  # magenta
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)
wn.exitonclick()