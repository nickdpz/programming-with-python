# !/ usr / bin / env python
# -* - coding : utf -8 -* -
import numpy as np
import matplotlib.pylab as plt
from scipy import special
nx = 1
ny = nx
wavelength = np.array([0.075, 0.0375, 0.0273])
D = np.linspace(-1, 1, 1000)
fig = plt.figure("Potter_Beam_pattern", figsize=(22, 12), facecolor ='white', edgecolor='blue')
fig.set_size_inches(15, 10)
theta = np.linspace(-np.pi, np.pi, 1000)
k = (2*np.pi)/(wavelength[2])
r = [0.1, 0.095, 0.105]
alpha = 0.653
K11E1 = 3.832/r[0]
K11H1 = 1.841/r[0]
betaH1 = np.sqrt(k**2-K11E1**2)
betaE1 = np.sqrt(k**2-K11H1**2)
P_potter1 = ((1+(betaH1*np.cos(theta)/k))-alpha*(((betaE1/k)+np.cos(theta))/(1 -(K11E1/(k*np.sin(theta)))**2)))*(special.jv(1, (k*r[0]*np.sin(theta)))/np.sin(theta))
K11E2 = 3.832/r[1]
K11H2 = 1.841/r[1]
betaH2 = np.sqrt(k**2-K11E2**2)
betaE2 = np.sqrt(k**2-K11H2**2)
P_potter2 = ((1+(betaH2*np.cos(theta)/k))-alpha*(((betaE2/k)+np.cos(theta))/(1 -(K11E2/(k*np.sin(theta)))**2)))*(special.jv(1, (k*r[0]*np.sin(theta)))/np.sin(theta))
K11E3 = 3.832/r[2]
K11H3 = 1.841/r[2]
betaH3 = np.sqrt(k**2-K11E3**2)
betaE3 = np.sqrt(k**2-K11H3**2)
P_potter3 = ((1+(betaH3*np.cos(theta)/k))-alpha*(((betaE3/k)+np.cos(theta))/(1-(K11E3/(k*np.sin(theta)))**2)))*(special.jv(1, (k*r[0]*np.sin(theta)))/np.sin(theta))
# P_potter1 = ( 1 - ( alpha /(1 - (3.832**2 / (* ( special . jv ( 1 , ( k * r [0]* np . sin ( theta ) )
# P_potter2 = ( 1 - ( alpha /(1 - (3.832**2 / (* ( special . jv ( 1 , ( k * r [1]* np . sin ( theta ) )
# P_potter3 = ( 1 - ( alpha /(1 - (3.832**2 / (* ( special . jv ( 1 , ( k * r [2]* np . sin ( theta ) )- alpha *((( betaE3 / k ) + np . cos (* ( special . jv ( 1 , ( k * r [0]* np . sin (( k * r [0]* np . sin ( theta ) ) **2) )) / k * r [0]* np . sin ( theta ) )( k * r [1]* np . sin ( theta ) ) **2) )) / k * r [1]* np . sin ( theta ) )( k * r [2]* np . sin ( theta ) ) **2) )) / k * r [2]* np . sin ( theta ) ))))))))))
ax = plt.subplot(131)
plt.plot(np.degrees(theta), 10*np.log10((P_potter2/np.amax(P_potter2))**2), 'b')
plt.title('a = ' + str(r[1]) + ' m ')
plt.ylim([-60, 0])
plt.xlabel(r'Angle $\theta$($\circ$)')
plt.ylabel('Power(dB)')
plt.legend()
ax = plt.subplot(132)
plt.plot(np.degrees(theta), 10*np.log10((P_potter1/np.amax(P_potter1))**2), 'g')
plt.title('a = ' + str(r[0]) + ' m ')
plt.xlabel(r'Angle $\theta$($\circ$)')
plt.ylabel('Power(dB)')
plt.ylim([-60, 0])
plt.legend()
ax = plt.subplot(133)
plt.plot(np.degrees(theta), 10*np.log10((P_potter3/np.amax(P_potter3))**2), 'purple')
plt.title('a = ' + str(r[2]) + ' m ')
plt.xlabel(r'Angle $\theta$($\circ$)')
plt.ylabel('Power(dB)')
plt.ylim([-60, 0])
plt.legend()
plt.tight_layout()
plt.savefig('Potter_Beam_pattern.png')
plt.show()