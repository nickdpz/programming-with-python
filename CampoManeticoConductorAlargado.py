#Nicolas Pastran cod:20151005087
#Katherin Castelblanco cod:20151005571

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import base64

z = base64.decodestring("QXV0b3IgTmljb2xhcyBEYXZpZCBQYXN0cmFuIFphbW9yYQ==")
fig = plt.figure(z, figsize=(13,2.5), facecolor = 'white',edgecolor='blue')
fig, ax = plt.subplots(figsize=(20,10),)
plt.subplots_adjust(left=0.15, bottom=0.30)

x = np.arange(0.01,5,0.01)
sigma = 5.96*10**7


H1=lambda x: np.piecewise(x,[x < 1. , x >= 1.],[1, 0])
H2 = lambda r: np.piecewise(x,[x < 1. , x >= 1.],[0, 1])
K= H1(x)*0.0002*x+H2(x)*0.0002/x

plt.axis([0,5,0,0.0003])


plt.plot(x,K,'blue',linewidth=2)
plt.figtext(0.5, 0.5, z , style='italic', wrap=True, horizontalalignment='center', fontsize=18, color='gray')

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

plt.title(r'$Campo $ $magnetico$ $ en$ $ el$  $interior$ $de$ $un$ $conductor$',fontdict=font3)
plt.xlabel(r'$Radio(milimetros)$', fontdict=font3)
plt.ylabel(r'$CampoMagnetico (Teslas) $', fontdict=font3)
plt.grid(True)


point, = plt.plot(x[1],K[1],"red",marker='o')



axcolor = 'black'
axfreq = plt.axes([0.15, 0.1, 0.7, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Freq', 0.1, 500, valinit=4)
msg=''

def update(val):
    freq = sfreq.val
    point.set_ydata(K[freq])
    point.set_xdata(x[freq])
    msg=r'$Radio=%f ,$  $ Campo Magnetico=%f$'%(x[freq],K[freq])
    fig.canvas.draw_idle()
    plt.legend([point], [msg],bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)
sfreq.on_changed(update)


plt.show()

#Nicolas Pastran cod:20151005087
#Katherin Castelblanco cod:20151005571