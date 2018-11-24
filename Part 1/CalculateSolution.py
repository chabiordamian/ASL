# zad7    #########################################
# Napisz skrypt obliczajacy pierwiastki rownania kwadratowego w postaci :
# y = ax2 + bx + c. Wejsciem skryptu sa wartosci: a, b, c
####################################################
import math
args = input("Podaj wspolczynniki a,b,c wielomianu.")
tuple(args)
a, b, c = tuple(float(x) for x in args.split(','))
delta = float(b**2 - 4*a*c)
if delta >= 0:
    sqrt_delta = math.sqrt(delta)
    x1 = (-b - sqrt_delta)/2*a
    x2 = (-b + sqrt_delta)/2*a
    results = [x1, x2]
    print(results)
else:
    print("Brak pierwiastkow rzeczywistych!")