from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(number):
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    root = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого '
          f'вами числа. Это будет: {root}')


print(message)
calc(25.5)
