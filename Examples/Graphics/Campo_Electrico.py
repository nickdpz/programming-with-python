#Nicolas Pastran cod:20151005087
#Katherin Castelblanco cod:20151005571

import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as sc
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots(figsize=(20,10))
plt.subplots_adjust(left=0.15, bottom=0.30)
po=0.000002
a=20
x = np.arange(0.01,40,0.01)

H1 = lambda x: np.piecewise(x,[x < 20. , x >= 20],[1, 0])
H2 = lambda x: np.piecewise(x,[x < 20. , x >= 20],[0, 1])

K= H1(x)*(po/sc.epsilon_0)*((x/3)-(x**3)/(5*a**2))+H2(x)*((a**3)/x**2)*(po/sc.epsilon_0)*(0.133333333)
k1=H2(x)*((a**3)/x**2)*(po/sc.epsilon_0)*(0.133333333)

plt.plot(x,K,'blue',linewidth=2,label="Campo Electrico Interno",color="blue")

plt.plot(x,k1, linewidth=2, label="Campo Electrico Externo",color="green")
plt.legend(loc=1)

font1 = {'family' : 'century',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 1,
        }

font2 = {'family' : 'century',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 1,
        }

font3 = {'family' : 'century',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 18,
        }
plt.title(r'$Campo$ $Electrico$ $ en$ $dentro$  $y$ $fuera$ $de$ $una$ $esfera$',fontdict=font3)
plt.xlabel(r'$Radio(m)$', fontdict=font3)
plt.ylabel(r'$Campo$ $Electrico(N/c)$', fontdict=font3)
plt.grid(True)


point, = plt.plot(x[1],K[1],"red",marker='o')



axcolor = 'black'
axfreq = plt.axes([0.15, 0.1, 0.7, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Radio', 1, 4000, valinit=4)
msg=''

def update(val):
    freq = sfreq.val
    point.set_ydata(K[freq])
    point.set_xdata(x[freq])
    msg=r'$Radio=%f ,$  $ Potencial=%f$'%(x[freq],K[freq])
    fig.canvas.draw_idle()
    plt.legend([point], [msg],bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)
sfreq.on_changed(update)


plt.show()
