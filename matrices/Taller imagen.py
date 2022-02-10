from scipy import misc
import scipy.signal
import numpy as np
#f = misc.face()
#f1 = np.array(f);
import requests
f = open('lena.jpg','wb')
f.write(requests.get('http://andadorurbano.com/wp-content/uploads/2017/09/len_top.jpg').content)
f.close()
f1 = misc.imread('lena.jpg')
#misc.imsave('face.png', f1) # uses the Image module (PIL)
f2=0.299*f1[:,:,0]
f3=0.587*f1[:,:,1]
f4=0.114*f1[:,:,2]
f5=f2+f3+f4
#print(f1)
#difuminar
#t = 1 - np.abs(np.linspace(-1, 1, 21))
#kernel = t.reshape(21, 1) * t.reshape(1, 21)
#kernel /= kernel.sum()   # kernel should sum to 1!  :)
 
# convolve 2d the kernel with each channel
#bordes
kernel=np.array([0,-1,0,-1,5,-1,0,-1,0]).reshape(3,3)
r = scipy.signal.convolve2d(f1[:,:,0], kernel, mode='same')
import matplotlib.pyplot as plt
plt.imshow(r)
plt.set_cmap('gray') 
plt.show()