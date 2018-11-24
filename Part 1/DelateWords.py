# zad9    #########################################
# Napisz skrypt usuwajacy z wejsciowego ciagu tekstowego (wybierz kilka
# plikow z repozytorium: Tekstowego) nastepujace slowa : sie, i, oraz,
# nigdy, dlaczego
####################################################
import os
import re

file = open("test.txt", "r")
lines = file.readlines()
forbidden_words = ["się", "oraz", "i", "prawie nigdy", "czemu"]
result = []

for line in lines:
    for forbidden_word in forbidden_words:
        line = (re.sub(r"\b{}\b".format(forbidden_word), "", line))
    result.append(line)
for line in result:
    print(line)
