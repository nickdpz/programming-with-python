import matplotlib.pyplot as plt

import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure("Dipolo electrico en dos dimensiones")

theta1 = np.arange(0.0, 2.0, 0.005) * np.pi
theta2 = np.arange(0.0, 2.0, 0.005) * np.pi
theta3 = np.arange(0.0, 2.0, 0.005) * np.pi
theta4 = np.arange(0.0, 2.0, 0.005) * np.pi
theta5 = np.arange(0.0, 2.0, 0.005) * np.pi
theta6 = np.arange(0.0, 2.0, 0.005) * np.pi

r1 = 1 * (np.sin(theta1 + (np.pi / 2))) ** 2
r2 = 2 * (np.sin(theta2 + (np.pi / 2))) ** 2
r3 = 4 * (np.sin(theta3 + (np.pi / 2))) ** 2
r4 = 6 * (np.sin(theta4 + (np.pi / 2))) ** 2
r5 = 8 * (np.sin(theta5 + (np.pi / 2))) ** 2
r6 = 9 * (np.sin(theta6 + (np.pi / 2))) ** 2


plt.polar(theta1, r1, color="#339FFF", linewidth=2)
plt.hold("true")
plt.polar(theta2, r2, color="#333FFF", linewidth=2)
plt.hold("true")
plt.polar(theta3, r3, color="#3352FF", linewidth=2)
plt.hold("true")
plt.polar(theta4, r4, color="#3371FF", linewidth=2)
plt.hold("true")
plt.polar(theta5, r5, color="#337DFF", linewidth=2)
plt.hold("true")
plt.polar(theta6, r6, color="#33B5FF", linewidth=2)
plt.hold("true")
plt.rgrids(np.arange(1.0, 9.0, 1.0), angle=90)
plt.show()
