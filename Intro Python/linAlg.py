import numpy as np

M = np.array([2,3,-15,-5,7,22,11,0,3]).reshape(3,3)
N = np.array([1,7,5,-2,8,-6,9,-4,3]).reshape(3,3)
C = np.array(range(16)).reshape(4,4)
A = np.array([3,1,-1,8,0,3,2,-5,-4]).reshape(3,3)
B = np.array([25,41,39]).reshape(3,1)
X = np.linalg.inv(A)@B
print("M + N:\n",M+N,"\n")
print("The dot product of M and N:\n",M@N,"\n")
print("The inverse of M:\n",np.linalg.inv(M),"\n")
print("The determinant of C:\n",np.linalg.det(C),"\n")
print("Solved system of equations:\n", X, "\n")
testString=input("Input numbers for your array:")
testArray = testString.split()
for i in range(len(testArray)):
    testArray[i] = int(testArray[i])
print(testArray)
if(np.all(np.diff(testArray) > 0)): print("True")
else: print("False")
