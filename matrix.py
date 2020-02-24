"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for n in range(len(matrix[0])):
        str = ""
        for col in matrix:
            str += "{}\t".format(col[n])
        print(str)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    i = 0
    while i < len(matrix):
        matrix[i][i] = 1
        i+=1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    matrix = new_matrix(rows = len(m1[0]), cols = len(m2))
    for i in range(len(matrix)):
        set1 = m2[i]
        for j in range(len(matrix[i])):
            set2 = [m1[n][j] for n in range(len(m1))]
            for h in range(len(set1)):
                matrix[i][j] += set1[h]*set2[h]
    return matrix


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
