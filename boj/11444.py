import sys

MAX_NUM = 1000000000000000000
DIVISOR = 1000000007

def matrix_mult(a,b):
    new_matrix = [[0,0],[0,0]]
    new_matrix[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % DIVISOR
    new_matrix[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % DIVISOR
    new_matrix[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % DIVISOR
    new_matrix[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % DIVISOR
    return new_matrix

def solve():
    n = int(sys.stdin.readline().strip())
    if n==0:
        return 0

    fibMatrixOfTwoPowers = [[] for _ in range(60)]
    reverted_bin_num = bin(n)[:1:-1]

    i = 0
    matrix = [[1,1],[1,0]]

    while 2**i <= MAX_NUM:
        fibMatrixOfTwoPowers[i] = matrix
        matrix = matrix_mult(matrix, matrix)
        i+=1

    res = [[1,0],[0,1]]
    for i in range(len(reverted_bin_num)):
        if reverted_bin_num[i] == '1':
            res = matrix_mult(res,fibMatrixOfTwoPowers[i])
    
    return res[0][1]

print(solve())