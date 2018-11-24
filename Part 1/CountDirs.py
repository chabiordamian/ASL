# zad3    #########################################
# Napisz skrypt zliczajacy ilosc plikow w katalogu /dev, skorzystaj ze standardowej
# biblioteki - os
####################################################
import os
counter = 0
try:
    n = os.scandir("/dev")
    for x in n:
        if x.is_file():
            counter += 1
    print(counter)
except FileNotFoundError:
    print("This path does not exist")
