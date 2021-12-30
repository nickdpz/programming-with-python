# Constantes de atenuación
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.widgets import Button

fig = plot.figure(
    "Constantes de Atenuacion", figsize=(20, 12), facecolor="white", edgecolor="blue"
)

x = np.linspace(0.05, 0.95, 1000)
condCu = 5.8 * (10 ** 7)
Cupper = np.sqrt(1 / (60 * x * condCu)) * ((1 + (x ** 2)) / np.sqrt(1 - (x ** 2)))
condAu = 4.5 * (10 ** 7)
Gold = np.sqrt(1 / (60 * x * condAu)) * ((1 + (x ** 2)) / np.sqrt(1 - (x ** 2)))
condAl = 3.54 * (10 ** 7)
Aluminium = np.sqrt(1 / (60 * x * condAl)) * ((1 + (x ** 2)) / np.sqrt(1 - (x ** 2)))

plot.subplots_adjust(bottom=0.1, left=0.25)
l, = plot.plot(x, Cupper, color="#FF8000", linewidth=3)
plot.grid(True)
plot.grid(color="0.1", linestyle="--", linewidth=1)
plot.xlabel(r"$\lambda$", fontsize=20, color="black")
plot.ylabel(r"$Kgi$", fontsize=20, color="black")
plot.title(
    r"$Constantes$ $de$ $atenuacion$",
    fontsize=24,
    color="black",
    verticalalignment="baseline",
    horizontalalignment="center",
)


class Index(object):
    def cupper(self, event):
        l.set_ydata(Cupper)
        l.set_color("#FF8000")
        plot.plot()

    def gold(self, event):
        l.set_ydata(Gold)
        l.set_color("gold")
        plot.plot()

    def aluminium(self, event):
        l.set_ydata(Aluminium)
        l.set_color("silver")
        plot.plot()


callback = Index()
dimCupper = plot.axes([0.05, 0.55, 0.1, 0.075])
btnCupper = Button(dimCupper, r"$Cobre$", color="#FF8000")
btnCupper.on_clicked(callback.cupper)
dimGold = plot.axes([0.05, 0.45, 0.1, 0.075])
btnGold = Button(dimGold, r"$Oro$", color="gold")
btnGold.on_clicked(callback.gold)
dimAluminium = plot.axes([0.05, 0.35, 0.1, 0.075])
btnAluminium = Button(dimAluminium, r"$Aluminio$", color="silver")
btnAluminium.on_clicked(callback.aluminium)
plot.show()
