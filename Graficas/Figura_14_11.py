#Figura 14.11
#Katherin Castelblanco - 20151005571
#Nicolas Pastran       - 20151005087

import numpy as np
import scipy.constants as constant
import matplotlib.pyplot as plot
import matplotlib.animation as animation
R=np.linspace(0.05,10, 1000)
figura=plot.figure('Figura 14.11',figsize=(20,10),facecolor = 'white',edgecolor='blue')
def update(t):
    plot.cla()
    plot.plot(R, np.sqrt(((1/R)**2)+1),'--', color='blue', linewidth = 1)
    plot.plot(R, -np.sqrt(((1/R)**2)+1),'--', color='blue', linewidth = 1)
    frame=landaK=np.sqrt(((1/R)**2)+1)*np.cos((0.1*t)-R+np.arctan(R))
    plot.plot(R, landaK, color='darkblue', linewidth = 3)
    plot.grid(True)
    plot.xlabel('$r/\lambdabar$', fontsize = 24, color = 'black')
    plot.ylabel('$k\lambdabar$', fontsize = 24, color = 'black')
    plot.title(r'Interseccion de superficie en $k\lambdabar$ para $\theta=\pi/2$',fontsize = 17, color = 'black', horizontalalignment = 'center')
    axes = plot.gca()
    axes.set_xlim([0,10])
    axes.set_ylim([-8,8])
    return frame,
animation=animation.FuncAnimation(figura, update, frames=180, interval=50)
plot.show()