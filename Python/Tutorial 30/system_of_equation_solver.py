import numpy as np
from scipy import linalg
# 2x + y + 3z = -2
# x - y - z = -3
# 3x - 2y - 12z = 3
a = np.array([[2,1,3],[1,-1,-1],[3,-2,-12]])
print(a)
b = np.array([[-2],[-3],[3]])
print(b)
answer = linalg.solve(a,b)
print(answer)
print("x=", round(answer[0,0],3),"y=", round(answer[1,0],3),"z=", round(answer[2,0],3))