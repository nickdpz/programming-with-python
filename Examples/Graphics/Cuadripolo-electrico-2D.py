# GRAFICA CUADRUPOLO ELECTRICO 2D

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure("Cuadrupolo electrico en 2D")

phi = np.linspace(0, np.pi, 100)
theta = np.arange(0, 2 * np.pi, 0.01)

r1 = 1 * (abs(np.sin(theta))) * ((abs(np.cos(theta))) ** 0.5)
r2 = 2 * (abs(np.sin(theta))) * ((abs(np.cos(theta))) ** 0.5)
r3 = 3 * (abs(np.sin(theta))) * ((abs(np.cos(theta))) ** 0.5)
r4 = 5 * (abs(np.sin(theta))) * ((abs(np.cos(theta))) ** 0.5)
r5 = 7 * (abs(np.sin(theta))) * ((abs(np.cos(theta))) ** 0.5)
r6 = 8 * (abs(np.sin(theta))) * ((abs(np.cos(theta))) ** 0.5)


y1 = plt.polar(theta, r1, color="#339FFF", linewidth=2)
y1 = plt.hold("true")
y2 = plt.polar(theta, r2, color="#333FFF", linewidth=2)
y2 = plt.hold("true")
y2 = plt.polar(theta, r3, color="#3352FF", linewidth=2)
y2 = plt.hold("true")
y3 = plt.polar(theta, r4, color="#3371FF", linewidth=2)
y3 = plt.hold("true")
y4 = plt.polar(theta, r5, color="#337DFF", linewidth=2)
y4 = plt.hold("true")
y5 = plt.polar(theta, r6, color="#33B5FF", linewidth=2)
y5 = plt.hold("true")

plt.rgrids(np.arange(1.0, 9.0, 1.0), angle=90)
plt.show()
