import numpy as np
A = np.linspace(1,48,48).reshape(3,4,4)
a = A[1][0][3]
b = A[0][2]
c = A[2]
d1 = A[0][1][0:2]
d2 = A[1][1][0:2]
d3 = A[2][1][0:2]
d=np.array([d1,d2,d3])
e1=A[2][0][2:5][::-1]
e2=A[2][1][2:5][::-1]
e3=A[2][2][2:5][::-1]
e4=A[2][3][2:5][::-1]
e=np.array([e1,e2,e3,e4])
f1=A[0].T[0][::-1]
f2=A[1].T[0][::-1]
f3=A[2].T[0][::-1]
f=np.array([f1,f2,f3])
g1=A[0][0][0]
g2=A[0][0][3]
g3=A[2][3][0]
g4=A[2][3][3]
g=np.array([g1,g2,g3,g4]).reshape(2,2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)