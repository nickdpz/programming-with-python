# !/ usr / bin / env python
#!/usr/bin/Python 2.7.12

import numpy as np
import matplotlib.pylab as plt
from scipy import special

nx = 1
ny = nx
wavelength = np.array([0.075, 0.0375, 0.0273])
D = np.linspace(-1, 1, 1000)
u = 1
theta = np.linspace(-np.pi/2, np.pi/2, 1000)
Lx = np.array([0.2, 0.4, 0.6])
Ly = np.linspace(-1, 1, 1000)
fig = plt.figure("Rectangular_x_Beam_pattern", figsize=(22,12), facecolor ='white', edgecolor='blue')
fig.set_size_inches(15, 10)
P_rectangular1 = (np.sin((np.pi*Lx[0]/wavelength[2])*np.sin(theta))/((np.pi*Lx[0]/wavelength[2])*np.sin(theta)))
P_rectangular2 = (np.sin((np.pi*Lx[1]/wavelength[2])*np.sin(theta))/((np.pi*Lx[1]/wavelength[2])*np.sin(theta)))
P_rectangular3 = (np.sin((np.pi*Lx[2]/wavelength[2])*np.sin(theta))/((np.pi*Lx[2]/wavelength[2])*np.sin(theta)))
ax = plt.subplot(131)
plt.plot(np.degrees(theta), 10*np.log10((P_rectangular1/np.amax(P_rectangular1))**2), 'b', label='0.2m')
plt.xlabel(r'Angle $\theta$($\circ$)')
plt.ylabel('Power(dB)')
plt.yticks(np.linspace(-40, 0, 5))
plt.ylim([-40, 0])
plt.grid(True)
plt.title('Dx = 0.2 m')
ax = plt.subplot(132)
plt.plot(np.degrees(theta), 10* np.log10((P_rectangular2/np.amax(P_rectangular2))**2), 'g', label='0.4m')
plt.xlabel(r'Dy $\theta$($\circ$)')
plt.ylabel('Power(dB)')
plt.yticks(np.linspace(-40, 0, 5))
plt.ylim([-40, 0])
plt.grid(True)
plt.title('Dx = 0.4 m')
ax = plt.subplot(133)
plt.plot (np.degrees(theta), 10*np.log10((P_rectangular3/np.amax(P_rectangular3))**2), 'purple', label=' 0.6 m')
plt.xlabel('Dy ( m )')
plt.ylabel(r'Power $\theta$($\circ$)')
plt.yticks(np.linspace(-40, 0, 5))
plt.ylim([-40, 0])
plt.grid(True)
plt.title('Dx = 0.6 m')
plt.tight_layout()
plt.savefig('Rectangular_x_Beam_pattern.png')
plt.show()