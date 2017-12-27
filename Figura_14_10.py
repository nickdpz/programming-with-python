#Figura 14.10
#Katherin Castelblanco - 20151005571
#Nicolas Pastran       - 20151005087

from mpl_toolkits.mplot3d import Axes3D
import scipy.constants as constant
import matplotlib.pyplot as plot
import numpy as np
from matplotlib import cm
import matplotlib.animation as animation

radio, theta = np.meshgrid(np.linspace(0.35, 10, 120),np.linspace(0, 2*np.pi, 100))
x = radio*np.cos(theta)
y = radio*np.sin(theta)

fig=plot.figure('Figura 14.10',figsize=(20,10))

def update(t):
	plot.cla()	
        ax = fig.add_subplot(111, projection='3d')
        plot.title('K$\lambda$ Por Nicolas Pastran y Katherin Castelblanco',fontsize = 30, color = 'black', verticalalignment = 'baseline', horizontalalignment = 'center')
        z = (np.sin(theta+constant.pi/2)**2)*(1/(radio**2)+1)*np.cos((0.8*t)-radio+np.arctan(radio));
        frame=ax.plot_surface(x,y,z, rstride=1, cstride=1, cmap='hot', vmin=-1.4, vmax=1.4, linewidth=.2)
        ax.set_zlim(-7, 7)
        ax.set_ylim(-7, 7)
        ax.set_xlim(-10, 10)
        ax.set_xlabel('x',fontsize=20)
        ax.set_ylabel('y',fontsize=20)
        ax.set_zlabel('z',fontsize=20)
        return frame,

animation=animation.FuncAnimation(fig, update, frames=180, interval=50)

plot.show()
