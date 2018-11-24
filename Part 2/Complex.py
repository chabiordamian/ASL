# #zad2    #########################################
# zdeniowa¢ klas¦ reprezentuj¡c¡ liczby zespolone (wraz z funkcjami na
# nich dziaªaj¡cymi np. moduª dodawanie, odejmowanie itd.),
####################################################
import math

class Complex(object):

    def __init__(self, re=0, im=0):
        self.re=re
        self.im=im

    def add(self, number_to_add):
        if type(number_to_add) == type(self):
            return Complex(self.re + number_to_add.re, self.im + number_to_add.im)
        else:
            raise ValueError("Wrong type!")

    def sub(self, number_to_sub):
        if type(number_to_sub) == type(self):
            return Complex(self.re - number_to_sub.re, self.im - number_to_sub.im)
        else:
            raise ValueError("Wrong type!")

    def abs(self):
        abs = self.re * self.re + self.im * self.im
        return math.sqrt(abs)

    def __str__(self):
        return str("{} + {}j".format(self.re, self.im))

x = Complex(3, 2)
y = Complex(4, 8)

print("{} + {} = {}".format(x, y, Complex.add(x, y)))
print("{} - ({}) = {}".format(x, y, Complex.sub(x, y)))
print("|{}| = {}".format(y, y.abs()))
