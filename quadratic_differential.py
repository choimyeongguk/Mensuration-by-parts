import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
y_ori = x**2
y_drv = []
for i in range(-10, 10): 
 y_drv.append(2*i*(x-i)+i**2)

plt.axis([-10, 10, -10, 100])
plt.plot(x, y_ori, color='red', linewidth='3')
for i in range(1,20):
 plt.plot(x, y_drv[i], color='blue', linewidth='1')
plt.show()