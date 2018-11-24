# zad15    #########################################
# Napisz skrypt wyliczajacy wyznacznik macierzy wygenerowanej losowo
####################################################
import random


def rand_matrix(x_size, y_size):
    matrix = []

    def rand_list(x_size):
        return [random.randint(0, 10) for x in range(x_size)]
    for x in range(y_size):
        matrix.append(rand_list(x_size))
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def determinant(matrix, lvl=1):
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            det = pow(-1, 1+lvl)*matrix[0][0]
            b = []
            for i in range(len(matrix)-1):
                b.append([])
                for j in range(len(matrix)-1):
                    b[i].append(matrix[i+1][j+1])
            det = det*determinant(b, lvl + 1)
            return det
    else:
        print("Matrix must be square!")


matrix = rand_matrix(random.randint(2, 2), random.randint(2, 2))
print_matrix(matrix)
print("\nDeterminant of this matrix is {}\n".format(determinant(matrix)))
