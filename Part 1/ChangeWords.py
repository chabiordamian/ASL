# zad10    #########################################
# Napisz skrypt zmieniajacy w podanym ciagu wejeciowym (wybierz kilka
# plikow z repozytorium: Tekstowego) nastepujace slowa : i, oraz, nigdy,
# dlaczego na nastepujacy zestaw slow : oraz, i, prawie nigdy, czemu. Zalecana
# struktura jest slownik.
####################################################
import os
import re

file = open("test.txt", "r")
lines = file.readlines()
forbidden_words_dict = {"i": "oraz", "oraz": "i", "nigdy": "prawie nigdy", "dlaczego": "czemu"}
result = []

for line in lines:
    for word, changed_word in forbidden_words_dict.items():
        line = (re.sub(r"\b{}\b".format(word), changed_word, line))
    result.append(line)
for line in result:
    print(line)
