import turtle

t = turtle.Turtle()


def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)
    t.rt(120)
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)


def snowflake(t, length):
    for i in range(3):
        koch(t, length)


snowflake(t, 1000)
turtle.mainloop()