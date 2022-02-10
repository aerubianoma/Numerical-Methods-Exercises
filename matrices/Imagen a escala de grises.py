from scipy import misc
import numpy as np
f = misc.face()
f1 = np.array(f);
misc.imsave('face.png', f1)
f2=0.299*f1[:,:,0]
f3=0.587*f1[:,:,1]
f4=0.114*f1[:,:,2]
f5=f2+f3+f4
import matplotlib.pyplot as plt

plt.imshow(f5)
plt.set_cmap('gray') 
plt.show()
