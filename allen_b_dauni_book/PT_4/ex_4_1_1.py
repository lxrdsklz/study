import turtle
pen = turtle.Turtle()


# start_state -> circle -> arc (t, r, 360) -> polyline(t, n, step_length, step_angle) -> end_state


def draw_arrow(f):
    f.fd(200)
    f.lt(160)
    f.fd(10)
    f.bk(10)
    f.lt(60)
    f.fd(10)
    f.bk(10)
    f.rt(220)


pen.write("Start State")
draw_arrow(pen)
pen.write('Circle(bob, radius)')
draw_arrow(pen)
pen.write('arc(t, r, 360)')
draw_arrow(pen)
pen.write('polyline(t, n, step_length, step_angle)')
draw_arrow(pen)
pen.write('End State')

turtle.mainloop()