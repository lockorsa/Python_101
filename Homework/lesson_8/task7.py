"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, re, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return f'({self.re}{"+" if self.im > 0 else ""}{self.im}j)'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        re = (self.re * other.re) - (self.im * other.im)
        im = (self.re * other.im) + (self.im * other.re)
        return ComplexNumber(re, im)


if __name__ == '__main__':
    a = ComplexNumber(5, 3)
    b = ComplexNumber(3, 6)
    c = ComplexNumber(10, -2)
    d = ComplexNumber(-8, 5)

    print(complex(5, 3) + complex(3, 6))
    print(complex(3, 6) + complex(10, -2))

    print(complex(5, 3) * complex(3, 6))
    print(complex(3, 6) * complex(10, -2))
    print(complex(10, -2) * complex(-8, 5))
