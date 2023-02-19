import turtle
t = turtle.Pen()
t.shape('turtle')
for i in range (10):
    t.pencolor('red')
    t.circle(i*5)
    t.left(5)
    t.pencolor('green')
    t.circle(i*10)
    t.left(10)
    t.pencolor('blue')
    t.circle(i*20)
    t.right(20)
