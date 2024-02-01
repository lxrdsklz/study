"""
if a < b + c: CANNOT DRAW A TRIANGLE
elif a + b == c: CAN (вырожденный)
else: CAN
"""


def is_triangle(a, b, c):
    if a < (b + c) and b < (a + c) and c < (a + b):
        print('Да')
    elif a + b == c:
        print('Да')
    else:
        print('Нет')


def triangle():
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))
    is_triangle(a, b, c)


triangle()