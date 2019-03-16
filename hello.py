#matrices calculator

#2x2 block

#input block matrix

A = [2, 1, 4, 3]

print ('Matrix A is:', A)

#input block matrix B

B = [-13, 26, -63, 44]

print ('Matrix B is:', B)

#matrix determ func 2

def matrix_determ(mataorb):
    return mataorb[0] * mataorb[3] - mataorb[2] * mataorb[1]

det_A = matrix_determ(A)
det_B = matrix_determ(B)

print ("Determent of matrix A is:",det_A)
print ("Determent of matrix B is:",det_B)

#matrix -1 inverse 2

def matrix_inverse(mataorb, detaorb):
    return 1/detaorb * mataorb[3]

A0 = matrix_inverse(A, det_A)
B0 = matrix_inverse(B, det_B)

def matrix_inverse_1(mataorb, detaorb):
    return 1/detaorb * -1 * mataorb[1]

A1 = matrix_inverse_1(A, det_A)
B1 = matrix_inverse_1(B, det_B)

def matrix_inverse_2(mataorb, detaorb):
    return 1/detaorb * -1 * mataorb[2]

A2 = matrix_inverse_2(A, det_A)
B2 = matrix_inverse_2(B, det_B)

def matrix_inverse_3(mataorb, detaorb):
    return 1/detaorb * mataorb[0]

A3 = matrix_inverse_3(A, det_A)
B3 = matrix_inverse_3(B, det_B)

Ainv = [A0, A1, A2, A3]
Binv = [B0, B1, B2, B3]

print ("Matrix A inverted is:", Ainv)
print ("Matrix B inverted is:", Binv)

#matrix summ

def matrix_sum(matrixA, matrixB):
        return[matrixA[0] + matrixB[0], matrixA[1] + matrixB[1], matrixA[2] + matrixB[2], matrixA[3] + matrixB[3]]

summat = matrix_sum(A, B)

print('Summ of matrix A and B is', summat)

#matrix mult int

def matrix_multint(matrix, inte):
    return [matrix[0] * inte , matrix[1] * inte, matrix[2] * inte, matrix[3] * inte]

inte = 3
multint = matrix_multint(A, inte)

print('Matrix multiplied by', inte, 'is', multint)

#matrix mult matrix

def matrix_multmatrix(matrixA, matrixB):
    return [matrixA[0] * matrixB[0] + matrixA[1] * matrixB[2], matrixA[0] * matrixB[1] + matrixA[1] * matrixB[3], matrixA[2] * matrixB[0] + matrixA[3] * matrixB[2], matrixA[2] * matrixB[1] + matrixA[3] * matrixB[3]]


multmatrix = matrix_multmatrix(A, B)

print('Mult of matrix A and B is', multmatrix)

#matrix inverse test

invtestA = matrix_multmatrix(A, Ainv)
invtestB = matrix_multmatrix(B, Binv)

print (invtestA, invtestB)

def matrixinvcheck(matrix, invmatrix):
    if matrix_multmatrix(matrix, invmatrix) == [1, 0, 0, 1]:
        print ('OK')
    else:
        print('Not OK')

matrixinvcheck(A, Ainv)
matrixinvcheck(B, Binv)

#matrix trans

Btrans = [B[0], B[2], B[1], B[3]]

print ('B trns is', Btrans)

result = [matrix_sum(matrix_sum(matrix_sum(matrix_multint(Ainv, det_B),  matrix_multmatrix(A, Btrans)), matrix_multint(matrix_multmatrix(B, B), -3)), matrix_multint(Binv, det_A))]

print('Home task result is', result)

print('-------------------END OF 2x2 MATRICES-------------------')

#matrix determ func 3