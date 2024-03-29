﻿# Graficas Finales
import numpy as np
import matplotlib.pyplot as plot
import base64
from matplotlib.widgets import Button
import matplotlib.pylab as plt
from scipy import special

nx = 1
ny = nx
z = base64.decodestring("QXV0b3IgTmljb2xhcyBEYXZpZCBQYXN0cmFuIFphbW9yYQ==")
wavelength = np.array([0.075, 0.0375, 0.0273])
D = np.linspace(-1, 1, 1000)
u = 1
fig = plot.figure(
    "Menu de Seleccion", figsize=(13, 2.5), facecolor="white", edgecolor="blue"
)
plot.figtext(
    0.5,
    0.8,
    "Which Beam pattern do you want ?",
    style="italic",
    wrap=True,
    horizontalalignment="center",
    fontsize=18,
)


class Index(object):
    def cupper(self, event):
        theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)
        Lx = np.array([0.2, 0.4, 0.6])
        Ly = np.linspace(-1, 1, 1000)
        fig = plt.figure(
            "Rectangular_x_Beam_pattern",
            figsize=(22, 12),
            facecolor="white",
            edgecolor="blue",
        )
        fig.set_size_inches(15, 10)
        P_rectangular1 = np.sin((np.pi * Lx[0] / wavelength[2]) * np.sin(theta)) / (
            (np.pi * Lx[0] / wavelength[2]) * np.sin(theta)
        )
        P_rectangular2 = np.sin((np.pi * Lx[1] / wavelength[2]) * np.sin(theta)) / (
            (np.pi * Lx[1] / wavelength[2]) * np.sin(theta)
        )
        P_rectangular3 = np.sin((np.pi * Lx[2] / wavelength[2]) * np.sin(theta)) / (
            (np.pi * Lx[2] / wavelength[2]) * np.sin(theta)
        )
        ax = plt.subplot(131)
        plt.figtext(
            0.5,
            0.5,
            z,
            style="italic",
            wrap=True,
            horizontalalignment="center",
            fontsize=18,
            color="gray",
        )
        plt.plot(
            np.degrees(theta),
            10 * np.log10((P_rectangular1 / np.amax(P_rectangular1)) ** 2),
            "b",
            label="0.2m",
        )
        plt.xlabel(r"Angle $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.yticks(np.linspace(-40, 0, 5))
        plt.ylim([-40, 0])
        plt.grid(True)
        plt.title("Dx = 0.2 m")
        ax = plt.subplot(132)
        plt.plot(
            np.degrees(theta),
            10 * np.log10((P_rectangular2 / np.amax(P_rectangular2)) ** 2),
            "g",
            label="0.4m",
        )
        plt.xlabel(r"Dy $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.yticks(np.linspace(-40, 0, 5))
        plt.ylim([-40, 0])
        plt.grid(True)
        plt.title("Dx = 0.4 m")
        ax = plt.subplot(133)
        plt.plot(
            np.degrees(theta),
            10 * np.log10((P_rectangular3 / np.amax(P_rectangular3)) ** 2),
            "purple",
            label=" 0.6 m",
        )
        plt.xlabel("Dy ( m )")
        plt.ylabel(r"Power $\theta$($\circ$)")
        plt.yticks(np.linspace(-40, 0, 5))
        plt.ylim([-40, 0])
        plt.grid(True)
        plt.title("Dx = 0.6 m")
        plt.tight_layout()
        plt.savefig("Rectangular_x_Beam_pattern.png")
        plt.show()

    def gold(self, event):
        Lx = np.array([0.2, 0.4, 0.6])
        Ly = np.linspace(-1, 1, 1000)
        u = 1.841
        r = [0.1, 0.3, 0.5]
        theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)
        fig = plt.figure(
            "Circular_Beam_pattern",
            figsize=(22, 12),
            facecolor="white",
            edgecolor="blue",
        )
        fig.set_size_inches(15, 10)
        P_circular1 = (wavelength[2] / (np.pi * r[0] * np.sin(theta))) * special.jn(
            1, ((2 * np.pi * r[0] * np.sin(theta)) / wavelength[2])
        )
        P_circular2 = (wavelength[2] / (np.pi * r[1] * np.sin(theta))) * special.jn(
            1, ((2 * np.pi * r[1] * np.sin(theta)) / wavelength[2])
        )
        P_circular3 = (wavelength[2] / (np.pi * r[2] * np.sin(theta))) * special.jn(
            1, ((2 * np.pi * r[2] * np.sin(theta)) / wavelength[2])
        )
        ax = plt.subplot(131)
        plt.plot(
            np.degrees(np.linspace(-np.pi / 2, np.pi / 2, 1000)),
            10 * np.log10((P_circular1 / np.amax(P_circular1)) ** 2),
            "b",
        )
        plt.title("a = " + str(0.1) + "m")
        plt.xlabel(r"Angle $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.grid(True)
        plt.ylim([-60, 0])
        plt.legend()
        ax = plt.subplot(132)
        plt.plot(
            np.degrees(np.linspace(-np.pi / 2, np.pi / 2, 1000)),
            10 * np.log10((P_circular2 / np.amax(P_circular2)) ** 2),
            "g",
        )
        plt.title("a = " + str(0.3) + "m")
        plt.xlabel(r"Angle $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.grid(True)
        plt.ylim([-60, 0])
        plt.legend()
        ax = plt.subplot(133)
        plt.plot(
            np.degrees(np.linspace(-np.pi / 2, np.pi / 2, 1000)),
            10 * np.log10((P_circular3 / np.amax(P_circular3)) ** 2),
            "purple",
        )
        plt.title("a = " + str(0.5) + "m")
        plt.xlabel(r"Angle $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.grid(True)
        plt.ylim([-60, 0])
        plt.legend()
        plt.title(r"$\lambda$=" + str(wavelength[1]))
        plt.tight_layout()
        plt.savefig("Circular_Beam_pattern.png")
        if z != 1:
            plt.show()
        else:
            print("Grafica")

    def aluminium(self, event):
        D = np.linspace(-1, 1, 1000)
        fig = plt.figure(
            "Potter_Beam_pattern", figsize=(22, 12), facecolor="white", edgecolor="blue"
        )
        fig.set_size_inches(15, 10)
        theta = np.linspace(-np.pi, np.pi, 1000)
        k = (2 * np.pi) / (wavelength[2])
        r = [0.1, 0.095, 0.105]
        alpha = 0.653
        K11E1 = 3.832 / r[0]
        K11H1 = 1.841 / r[0]
        betaH1 = np.sqrt(k ** 2 - K11E1 ** 2)
        betaE1 = np.sqrt(k ** 2 - K11H1 ** 2)
        P_potter1 = (
            (1 + (betaH1 * np.cos(theta) / k))
            - alpha
            * (
                ((betaE1 / k) + np.cos(theta))
                / (1 - (K11E1 / (k * np.sin(theta))) ** 2)
            )
        ) * (special.jv(1, (k * r[0] * np.sin(theta))) / np.sin(theta))
        K11E2 = 3.832 / r[1]
        K11H2 = 1.841 / r[1]
        betaH2 = np.sqrt(k ** 2 - K11E2 ** 2)
        betaE2 = np.sqrt(k ** 2 - K11H2 ** 2)
        P_potter2 = (
            (1 + (betaH2 * np.cos(theta) / k))
            - alpha
            * (
                ((betaE2 / k) + np.cos(theta))
                / (1 - (K11E2 / (k * np.sin(theta))) ** 2)
            )
        ) * (special.jv(1, (k * r[0] * np.sin(theta))) / np.sin(theta))
        K11E3 = 3.832 / r[2]
        K11H3 = 1.841 / r[2]
        betaH3 = np.sqrt(k ** 2 - K11E3 ** 2)
        betaE3 = np.sqrt(k ** 2 - K11H3 ** 2)
        P_potter3 = (
            (1 + (betaH3 * np.cos(theta) / k))
            - alpha
            * (
                ((betaE3 / k) + np.cos(theta))
                / (1 - (K11E3 / (k * np.sin(theta))) ** 2)
            )
        ) * (special.jv(1, (k * r[0] * np.sin(theta))) / np.sin(theta))
        # P_potter1 = ( 1 - ( alpha /(1 - (3.832**2 / (* ( special . jv ( 1 , ( k * r [0]* np . sin ( theta ) )
        # P_potter2 = ( 1 - ( alpha /(1 - (3.832**2 / (* ( special . jv ( 1 , ( k * r [1]* np . sin ( theta ) )
        # P_potter3 = ( 1 - ( alpha /(1 - (3.832**2 / (* ( special . jv ( 1 , ( k * r [2]* np . sin ( theta ) )- alpha *((( betaE3 / k ) + np . cos (* ( special . jv ( 1 , ( k * r [0]* np . sin (( k * r [0]* np . sin ( theta ) ) **2) )) / k * r [0]* np . sin ( theta ) )( k * r [1]* np . sin ( theta ) ) **2) )) / k * r [1]* np . sin ( theta ) )( k * r [2]* np . sin ( theta ) ) **2) )) / k * r [2]* np . sin ( theta ) ))))))))))
        ax = plt.subplot(131)
        plt.plot(
            np.degrees(theta), 10 * np.log10((P_potter2 / np.amax(P_potter2)) ** 2), "b"
        )
        plt.title("a = " + str(r[1]) + " m ")
        plt.ylim([-60, 0])
        plt.xlabel(r"Angle $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.legend()
        ax = plt.subplot(132)
        plt.plot(
            np.degrees(theta), 10 * np.log10((P_potter1 / np.amax(P_potter1)) ** 2), "g"
        )
        plt.title("a = " + str(r[0]) + " m ")
        plt.xlabel(r"Angle $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.ylim([-60, 0])
        plt.legend()
        ax = plt.subplot(133)
        plt.plot(
            np.degrees(theta),
            10 * np.log10((P_potter3 / np.amax(P_potter3)) ** 2),
            "purple",
        )
        plt.title("a = " + str(r[2]) + " m ")
        plt.xlabel(r"Angle $\theta$($\circ$)")
        plt.ylabel("Power(dB)")
        plt.ylim([-60, 0])
        plt.legend()
        plt.tight_layout()
        plt.savefig("Potter_Beam_pattern.png")
        plt.show()


callback = Index()

dimCupper = plot.axes([0.02, 0.26, 0.3, 0.2])
btnCupper = Button(dimCupper, "Rectangular_x_Beam_pattern", color="#21a7f4")
btnCupper.on_clicked(callback.cupper)
dimGold = plot.axes([0.35, 0.26, 0.3, 0.2])
btnGold = Button(dimGold, "Circular_Beam_pattern", color="#21a7f4")
btnGold.on_clicked(callback.gold)
dimAluminium = plot.axes([0.68, 0.26, 0.3, 0.2])
btnAluminium = Button(dimAluminium, "Potter_Beam_pattern", color="#21a7f4")
btnAluminium.on_clicked(callback.aluminium)
plot.show()
