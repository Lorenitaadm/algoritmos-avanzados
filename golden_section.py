from math import sqrt
from turtle import done, rt, fd, pensize, pencolor, circle, lt, speed, hideturtle

PHI = 2 / (sqrt(5) - 1)

# def square():
#     for _ in range(4):
#         fd(50)
#         rt(90)

# #print(PHI)
# #pensize(5)
# #pencolor('#F30CC6')
# #square()
# #pencolor('blue')
# #circle(100,90)
# #done()

# def golden_spiral(n):
#     size = 5
#     for _ in range(n):
#         circle(size, 90)
#         size *= PHI

# golden_spiral(10)
# done()


#2
# def square(size):
#     for _ in range(4):
#         fd(size)
#         rt(90)

# def golden_spiral(n):
#     size = 5
#     for _ in range(n):
#         square(size)
#         circle(size, 90)
#         size *= PHI

# golden_spiral(9)
# done()



def square(size):
    for _ in range(4):
        fd(size)
        lt(90)

def golden_spiral(n):
    size = 5
    for _ in range(n):
        pencolor('green')
        square(size)
        pencolor('orange')
        circle(size, 90)
        size *= PHI

speed('fastest')
hideturtle()
pensize(3)
golden_spiral(10)
done()


