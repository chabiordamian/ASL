# zad9     #########################################
# Napisz skrypt sortujacy liczby malejaco. Wygeneruj losowo 50 liczb -
# wykorzystaj standardowa funkcje do losowania. Z wbudowanej funkcji
# sortujacej korzystaj tylko w celu weryfkacji wynikow
####################################################
import random
unsorted_list = []
sorted_list = []
for x in range(50):
    unsorted_list.append(random.randrange(100))
print (unsorted_list)
while unsorted_list:
    biggest = unsorted_list[0]
    for index in range(len(unsorted_list)):
        if unsorted_list[index]>biggest:
            biggest = unsorted_list[index]
    unsorted_list.remove(biggest)
    sorted_list.append(biggest)
print(sorted_list)