#Figura 14.9
#Nicolas Pastran        -  20151005087
#Katherine Casteblanco  - 20151005571
import numpy as np
import scipy.constants as constant
import matplotlib.pyplot as plot
from matplotlib.widgets import Slider

fig=plot.figure('Fuerza electrica de un Dipolo Oscilante - Figura 14.9',figsize=(20,10),facecolor = 'white',edgecolor='blue')
radio,theta =np.meshgrid(np.linspace(0,10,500),np.linspace(0,2*constant.pi,500))
x=radio*np.cos(theta);
y=radio*np.sin(theta);
wt=constant.pi
contour_axes=fig.add_subplot(111)
plot.title('Presentado por Nicolas Pastran y Katherin Castelblanco',fontsize = 15, color = 'black', horizontalalignment = 'center')
plot.subplots_adjust(bottom=0.25)
F = ((np.sin(theta+constant.pi/2))**2)*np.cos(wt-radio+np.arctan(radio))
frame=plot.contour(x,y,F,10, linewidths=(2,),colors=('yellow', 'blue', 'red','black'))
plot.grid(True,color='0.5',linestyle='--', linewidth=1,ydata=[-10,10],xdata=[-10,10])
contour_axes = plot.gca()
contour_axes.set_xlim([-10,10])
contour_axes.set_ylim([-10,10])
axcolor = 'white'
axWt = plot.axes([0.2, 0.1, 0.6, 0.05], axisbg=axcolor)
sldWt = Slider(axWt, '$\omega$$t$', 0.0, 2.0*constant.pi, valinit=0)
def update(val):
    wt = sldWt.val
    F = ((np.sin(theta+constant.pi/2))**2)*np.cos(wt-radio+np.arctan(radio))
    contour_axes.clear()
    contour_axes.contour(x,y,F,10,linewidths=(2,),colors=('yellow', 'blue', 'red','black'))
    contour_axes.set_title('Presentado por Nicolas Pastran y Katherin Castelblanco',fontsize = 15, color = 'black', verticalalignment = 'baseline', horizontalalignment = 'center')
    contour_axes.grid(True)
    contour_axes.grid(color='0.5',linestyle='--', linewidth=1,ydata=[-10,10],xdata=[-10,10])
sldWt.on_changed(update)
plot.show()