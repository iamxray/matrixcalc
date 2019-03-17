#matrices calculator v 100500

#2x2 block

#input block matrix

inp = input('Add Matix A, separated by space:')
A = list(map(float, inp.split()))

#A = [0, 0, 0, 0]

print ('Matrix A is:', A)

#input block matrix B

inp = input('Add Matix B, separated by space:')
B = list(map(float, inp.split()))

#B = [1, 2, 3, 4]

print ('Matrix B is:', B)

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


#matrix trans

Btrans = [B[0], B[2], B[1], B[3]]

print ('B trns is', Btrans)

#matrix determ func 2

def matrix_determ(mataorb):
    return mataorb[0] * mataorb[3] - mataorb[2] * mataorb[1]

det_A = matrix_determ(A)
det_B = matrix_determ(B)

print ("Determent of matrix A is:",det_A)
print ("Determent of matrix B is:",det_B)

#Matrix inverse pos check det != 0

def matrix_inverse(mataorb, detaorb):
    if detaorb == 0:
        raise SystemExit("Matrix", mataorb, "cannot be inverted, determent = 0.")
    else:
        return [(1 / detaorb * mataorb[3]), (1 / detaorb * -1 * mataorb[1]), (1 / detaorb * -1 * mataorb[2]), (1 / detaorb * mataorb[0])]


Ainv = matrix_inverse(A, det_A)
Binv = matrix_inverse(B, det_B)

print("Matrix A inverted is:", Ainv)
print("Matrix B inverted is:", Binv)

#matrix inverse test

invtestA = matrix_multmatrix(A, Ainv)
invtestB = matrix_multmatrix(B, Binv)

def matrixinvcheck(matrix, invmatrix):
    if matrix_multmatrix(matrix, invmatrix) == [1, 0, 0, 1]:
        print ('Matrix',matrix,'invert check OK')
    else:
        print('Matrix' ,matrix,'invert check NOT OK')

matrixinvcheck(A, Ainv)
matrixinvcheck(B, Binv)

result = [matrix_sum(matrix_sum(matrix_sum(matrix_multint(Ainv, det_B),  matrix_multmatrix(A, Btrans)), matrix_multint(matrix_multmatrix(B, B), -3)), matrix_multint(Binv, det_A))]

print('Home task result is', result)

print('-------------------END OF 2x2 MATRICES-------------------')

#matrix determ func 3

#3x3 block

#input block matrix

#inp = input('Add Matix A, separated by space:')
#A = list(map(float, inp.split()))

A = [1.0, -5.0, 12.0, 7.0, 6.0, 2.0, 3.0, 9.0, 4.0]

print ('Matrix A is:')
print ('(', A[0], A[1], A[2],')')
print ('(', A[3], A[4], A[5],')')
print ('(', A[6], A[7], A[8],')')

#Det 3x3 first way

det3x3_1 = ((A[0] * A[4] * A[8]) + (A[1] * A[5] * A[6]) + (A[3] * A[7] * A[2])) - ((A[6] * A[4] * A[2]) + (A[7] * A[5] * A[0]) + (A[3] * A[1] * A[8]))

print (det3x3_1)

def matrix3_multinv(matrix, inte):
    return [matrix[0] * inte , matrix[3] * inte, matrix[6] * inte, matrix[1] * inte, matrix[4] * inte, matrix[7] * inte, matrix[2] * inte, matrix[5] * inte, matrix[8] * inte]

inte = 1 / det3x3_1
multinv = matrix3_multinv(A, inte)

print(inte, 'Matrix', A , 'invert is', multinv)