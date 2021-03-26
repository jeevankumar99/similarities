from enum import Enum
from cs50 import get_string
from operator import itemgetter


# this creates a struct like thing that stores which op is performed
class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


# these two are useless, they are used to help out in other programs
m = 0
n = 0


# this is to get the length of string1 before function
def ls1(x):
    m = len(x)
    return m


# this is to get the lenght of string2 before function
def ls2(y):
    n = len(y)
    return n


# this is to be returned to applications.py as a seperate string to create a table
org_matrix = [[0 for y in range(n + 1)] for y in range(m + 1)]


# the main function, yeah this is what all the fuss whas about
def distances(a, b):
    matrix = [[0 for x in range(len(b) + 1)] for x in range(len(a) + 1)]
    matrix_op = [[0 for y in range(len(b) + 1)] for y in range(len(a) + 1)]
    m = len

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):

            if i == 0:
                matrix[i][j] = j
                matrix_op[i][j] = Operation.INSERTED

            elif j == 0:
                matrix[i][j] = i
                matrix_op[i][j] = Operation.DELETED

            elif a[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
                matrix_op[i][j] = Operation.SUBSTITUTED

            # this is to find out which is operation is perfomred with the fewest steps
            else:
                matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])

                if matrix[i][j] == 1 + matrix[i][j - 1]:
                    matrix_op[i][j] = Operation.INSERTED

                elif matrix[i][j] == 1 + matrix[i - 1][j]:
                    matrix_op[i][j] = Operation.DELETED

                elif matrix[i][j] == 1 + matrix[i - 1][j - 1]:
                    matrix_op[i][j] = Operation.SUBSTITUTED

    # this is the final tuple list, the operation count and type of operation list is combined
    final_matrix = [[(0, 0) for i in range(len(b) + 1)]for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            final_matrix[i][j] = (matrix[i][j], matrix_op[i][j])
            final_matrix[0][0] = (0, None)

    return final_matrix


# this does half of what the first function does, it returns on the number of ops permformed
def orgdistance(a, b):
    matrix2 = [[0 for x in range(len(b) + 1)] for x in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):

            if i == 0:
                matrix2[i][j] = j

            elif j == 0:
                matrix2[i][j] = i

            elif a[i-1] == b[j-1]:
                matrix2[i][j] = matrix2[i-1][j-1]

            else:
                matrix2[i][j] = 1 + min(matrix2[i][j - 1], matrix2[i - 1][j], matrix2[i - 1][j - 1])

    return matrix2

# so basically the whole program is filled with comments, it seems I have to add more.
# yeah and here comes another
# and another one again
# that should do