import numpy as np
from numpy.linalg import inv, solve
import matplotlib as plt

'''
x = np.arange(0.0, 6.2, 0.1)
plt.pyplot.plot(x, np.sin(x), 'o-', x, np.cos(x), '^-', markersize=3)
plt.pyplot.xlabel('x')
plt.pyplot.legend(('sine', 'cosine'), loc=0)
plt.pyplot.savefig('testplot', format='tiff')
plt.pyplot.show()
'''


A = np.array([[4.0, -2.0, 1.0],
           [-2.0, 4.0, -2.0],
           [1.0, -2.0, 3.0]])
b = np.array([[1.0, 4.0, 2.0]])
print(b.T.shape)
A_inv = inv(A)
result = solve(A, b.T)
print(result, '\n')
print(np.dot(A_inv, b.T))
print(np.dot(A_inv, A))

'''
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
