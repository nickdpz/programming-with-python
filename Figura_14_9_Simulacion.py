#-figura 14.9 Simulacion 
#Katherin Castelblanco - 20151005571
#Nicolas Pastran       - 20151005087


import numpy as np
import scipy.constants as constant
import matplotlib.pyplot as plot
import matplotlib.animation as animation
import base64


radio,theta =np.meshgrid(np.linspace(0,20,1000),np.linspace(0,2*constant.pi,1000))
x=radio*np.cos(theta);
y=radio*np.sin(theta);
wt=constant.pi
p = base64.decodestring("QXV0b3IgTmljb2xhcyBEYXZpZCBQYXN0cmFuIFphbW9yYQ==")

fig=plot.figure('Fuerza Electrica de un Dipolo Oscilante Figura 14.9',figsize=(20,10),facecolor = 'white',edgecolor='blue')
plot.figtext(0.5, 0.5, p , style='italic', wrap=True, horizontalalignment='center', fontsize=18, color='gray')

contour_axes=fig.add_subplot(111)
def update(t):
	plot.cla()	
	plot.title('Presentado por Nicolas Pastran y Katherin Castelblanco',fontsize = 25, color = 'black', verticalalignment = 'baseline', horizontalalignment = 'center')
        z = ((np.sin(theta+constant.pi/2))**2)*np.cos(0.1*t-radio+np.arctan(radio))
        frame=plot.contour(x,y,z,10,  linewidths=(2,),colors=('yellow', 'blue', 'red','black'))
        contour_axes.set_xlim([-10,10])
        contour_axes.set_ylim([-10,10])
        plot.grid(True)
        plot.grid(color='0.5',linestyle='--', linewidth=1,ydata=[-10,10],xdata=[-10,10])
	return frame,

animation=animation.FuncAnimation(fig, update, frames=180, interval=30)

plot.show()