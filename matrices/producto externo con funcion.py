import numpy as np
A = np.arange(0,9).reshape(3,3);
B = np.array([1,3,5,8,9,5,7,1,6]).reshape(3,3);
print((A)*(B.T))