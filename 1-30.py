import numpy as np
from math import pi, sqrt, sin

x = 0.0
s = 0.0

for i in range(101):
    s += sqrt(i*pi/100)*sin(i*pi/100)
print(s)

y = np.arange(0, 1.001*pi, 0.01*pi)
print(sum(np.sqrt(y)*np.sin(y)))



'''
A = np.array([[4, -2, 1], 
              [-2, 4, -2],
              [1, -2, 3]])
b = np.array([1, 4, 2])

print(np.linalg.solve(A, b))
'''
'''
B = A.copy()
B[0] = ([9,9,9,0,36,144])
print(B[0, 0:])
print(np.sqrt(B[0, 0:3]))
'''
'''
nMax = 7
val = 1
counter = val
list_empty = []
while counter <= nMax:
    list_empty.append(1.0/counter)
    counter+=1
    print(counter-1, '\n')
print(list_empty, '\n')
print(val, counter)

def sign_a(a):
    if a > 0:
        sign = 'positive'
    elif a < 0:
        sign = 'negative'
    else:
        sign = 'zero'
    return sign

b = 9
print('the sign of a is ', sign_a(b), ' Bitch')

a = [1.0, 2.0, 3.0]
print('a =', a)
b = a
b[0] = 0.5
print('b = ', b)
print('a =', a)
c = a[:]
c[0] = 7.0
print('c = ', c)
print('a = ', a)
'''