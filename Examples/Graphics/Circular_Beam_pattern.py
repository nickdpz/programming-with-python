# !/ usr / bin / env python
# -* - coding : utf -8 -* -

import numpy as np
import matplotlib.pylab as plt
from scipy import special

nx = 1
ny = nx
wavelength = np.array([0.075, 0.0375, 0.0273])
D = np.linspace(-1, 1, 1000)
theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)
Lx = np.array([0.2, 0.4, 0.6])
Ly = np.linspace(-1, 1, 1000)
u = 1.841
r = [0.1, 0.3, 0.5]
theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)
fig = plt.figure(
    "Circular_Beam_pattern.png", figsize=(22, 12), facecolor="white", edgecolor="blue"
)
fig.set_size_inches(15, 10)
P_circular1 = (wavelength[2] / (np.pi * r[0] * np.sin(theta))) * special.jn(
    1, ((2 * np.pi * r[0] * np.sin(theta)) / wavelength[2])
)
P_circular2 = (wavelength[2] / (np.pi * r[1] * np.sin(theta))) * special.jn(
    1, ((2 * np.pi * r[1] * np.sin(theta)) / wavelength[2])
)
P_circular3 = (wavelength[2] / (np.pi * r[2] * np.sin(theta))) * special.jn(
    1, ((2 * np.pi * r[2] * np.sin(theta)) / wavelength[2])
)
ax = plt.subplot(131)
plt.plot(
    np.degrees(np.linspace(-np.pi / 2, np.pi / 2, 1000)),
    10 * np.log10((P_circular1 / np.amax(P_circular1)) ** 2),
    "b",
)
plt.title("a = " + str(0.1) + "m")
plt.xlabel(r"Angle $\theta$($\circ$)")
plt.ylabel("Power(dB)")
plt.grid(True)
plt.ylim([-60, 0])
plt.legend()
ax = plt.subplot(132)
plt.plot(
    np.degrees(np.linspace(-np.pi / 2, np.pi / 2, 1000)),
    10 * np.log10((P_circular2 / np.amax(P_circular2)) ** 2),
    "g",
)
plt.title("a = " + str(0.3) + "m")
plt.xlabel(r"Angle $\theta$($\circ$)")
plt.ylabel("Power(dB)")
plt.grid(True)
plt.ylim([-60, 0])
plt.legend()
ax = plt.subplot(133)
plt.plot(
    np.degrees(np.linspace(-np.pi / 2, np.pi / 2, 1000)),
    10 * np.log10((P_circular3 / np.amax(P_circular3)) ** 2),
    "purple",
)
plt.title("a = " + str(0.5) + "m")
plt.xlabel(r"Angle $\theta$($\circ$)")
plt.ylabel("Power(dB)")
plt.grid(True)
plt.ylim([-60, 0])
plt.legend()
# plt.title(r'$\lambda$=' + str(wavelength[1]))
plt.tight_layout()
plt.savefig("Circular_Beam_pattern.png")
plt.show()
