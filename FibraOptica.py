#Fibra Optica
#Katherin Castelblanco - 20151005571
#Nicolas Pastran       - 20151005087
import numpy as np
import scipy.constants as constant
import matplotlib.pyplot as plt
import base64
from matplotlib.widgets import Slider


a=1
w = 2
E = 5*constant.pi
z = base64.decodestring("QXV0b3IgTmljb2xhcyBEYXZpZCBQYXN0cmFuIFphbW9yYQ==")

fig=plt.figure('Fibra Optica - Nicolas Pastran',figsize=(22,12),facecolor = 'white',edgecolor='blue')
plt.subplot(1,1,1)
plt.subplots_adjust(bottom=0.18)

alpha=np.linspace(0,10*constant.pi, 1000,endpoint=True)
grafica1=np.tan(0.5*alpha*a)
grafica2=-1/np.tan(0.5*alpha*a)
grafica3=((w**2)*E/(alpha**2))-1
l1, = plt.plot(alpha, grafica1, lw=2, color='green')
l2, = plt.plot(alpha, grafica2, lw=2, color='blue')
l3, = plt.plot(alpha, grafica3, lw=2, color='red')


plt.xlabel(r'$\alpha$', fontsize = 24, color = 'blue')
plt.ylabel(r'$\beta/\alpha$', fontsize = 24, color = 'red')
plt.title('Fibra Optica',fontsize = 25, color = 'black', horizontalalignment = 'center')
#plt.title('Nicolas Pastran y Katherin Castelblanco',fontsize = 15, color = 'drackblue', verticalalignment = 'baseline', horizontalalignment = 'center')

plt.xlim([0,10*constant.pi])
plt.ylim([0,5])
#plt.yticks(np.linspace(1,5,4,endpoint=True),fontsize = 14, color = 'black')
plt.figtext(0.5, 0.5, z , style='italic', wrap=True, horizontalalignment='center', fontsize=18, color='gray')
plt.xticks([0, constant.pi,2*constant.pi,3*constant.pi,4*constant.pi,5*constant.pi,6*constant.pi,7*constant.pi,8*constant.pi,9*constant.pi,10*constant.pi],
           [r'$0$',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$',r'$5\pi$',r'$6\pi$',r'$7\pi$',r'$8\pi$',r'$9\pi$',r'$10\pi$'],fontsize = 17, color = 'black')
plt.grid(True)
plt.grid(color='0.1',linestyle='--', linewidth=2)
axes = plt.gca()
#Slider
axcolor = 'white'
axE = plt.axes([0.2, 0.04, 0.65, 0.05], axisbg=axcolor)
sldE = Slider(axE, r'$\epsilon$',0.5, 250.0, valinit=E)



def update(val):
    E = sldE.val
    l1.set_ydata(np.tan(0.5*alpha*a))
    l2.set_ydata(-1/np.tan(0.5*alpha*a))
    l3.set_ydata(((w**2)*E/(alpha**2))-1)
    fig.canvas.draw_idle()
sldE.on_changed(update)
if z != 1:
    plt.show()
else :
   print('Hola')   