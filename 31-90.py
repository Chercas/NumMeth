import numpy as np

#Vandermode matrix
def Vandermonde(v):
    n = len(v)
    a = np.zeros((n, n))
    for j in range(n):
        a[:,j] = v**(n-j-1)
    return a
    
v = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
b = np.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
a = Vandermonde(v)
print(a)
A = a.copy()
B = b.copy()

##Go to ass elimination

'''
Solves [A]<x|=<b| by Gauss elimination 
'''
'''
def gaussElimin(a,b):
    n = len(b)
# Elimination Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
# Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
        return b


'''
def gaussElimin(a,b):
    n = len(b)
# Elimination Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
                b[i] = b[i] - lam*b[k]
    print(a, '\n', b)

    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

Y = gaussElimin(a, b)
determinant = np.prod(np.diagonal(a))
print('Y=\n', Y)
print('\ndet = ', determinant)
print('\nCheck result: [a]{Y} - b =\n',np.dot(A,Y) - B)

'''
A = np.array([[5, 4, 8, 1],
              [0, 3, 7, -4],
              [8, 0, 4, -2],
              [-1, 6, 0, 2]])    
b = np.array([ [7], [-46], [0], [13]])
#print(A.shape, '\n', b.shape)
print(gaussElimin(A,b))
'''