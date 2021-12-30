# GRAFICA DIPOLO ELECTRICO 3D


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure("Dipolo electrico en 3D")

ax = fig.gca(projection="3d")

u = np.linspace(0, 4 * np.pi, 60)
v = np.linspace(-np.pi, np.pi, 80)
u, v = np.meshgrid(u, v)

r = ((np.sin(u) + np.pi / 2)) ** 2
x = (r * (np.sin(u) * np.cos(v))).flatten()
y = (r * (np.sin(u) * np.sin(v))).flatten()
z = (r * (np.cos(u))).flatten()

ax.plot_trisurf(x, y, z, cmap=plt.cm.seismic)


plt.show()
