# zad11    #########################################
# Napisz skrypt obliczajacy wartosciloczynu dwoch wektorow : a = [1, 2,
# 12, 4], b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorow
####################################################
a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
result = [a*b for a, b in zip(a, b)]
print(list(result))