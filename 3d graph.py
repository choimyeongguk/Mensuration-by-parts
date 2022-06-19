from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure(figsize=(7, 7))
ax3d = plt.axes(projection='3d')

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = 1/(1+np.exp(-X, -Y))

ax3d.plot_surface(X, Y, Z, cmap='plasma')
plt.show()