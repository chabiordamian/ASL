# zad13    #########################################
# Napisz skrypt sumujacy dwie macierze o rozmiarach 128x128. Wykorzystaj
# generator liczb losowych do wygenerowania macierzy. Zrealizuj operacje
# z wykorzystaniem
####################################################
import random

matrix_x_size = 128
matrix_y_size = 128


def rand_matrix(x_size, y_size):
    matrix = []

    def rand_list(x_size):
        return [random.randint(0, 999) for x in range(x_size)]
    for x in range(y_size):
        matrix.append(rand_list(x_size))
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def add(a, b):
    result = []
    for i in range(len(a)):
        row=[]
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        result.append(row)
    return result


a = rand_matrix(matrix_x_size, matrix_y_size)
b = rand_matrix(matrix_x_size, matrix_y_size)
print_matrix(a)
print("+")
print_matrix(b)
print("=")
print_matrix(add(a, b))