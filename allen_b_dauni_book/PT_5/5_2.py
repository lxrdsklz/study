# theorem = a ** n + b ** n = c ** n

def check_fermat(a, b, c, n):
    if n > 2:
        if a ** n + b ** n == c * n:
            print('Не может быть, Ферма ошибся!')
        else:
            print('Нет, это не работает')
    else:
        print('Error: N < 2')


def inputs():
    a = int(input('Input a: '))
    b = int(input('Input b: '))
    c = int(input('Input c: '))
    n = int(input('Input n: '))
    check_fermat(a, b, c, n)


inputs()