import turtle
victor = turtle.Turtle()
for i in range(13):
    for j in range(3):
        victor.speed(10)
        for k in range(2):
            victor.forward(100)
            victor.right(120)
        victor.forward(100)
    victor.right(5)
turtle.done()