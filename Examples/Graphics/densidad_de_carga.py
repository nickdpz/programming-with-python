import matplotlib.pyplot as plt
import numpy as np
import base64

fig = plt.figure(
    "Densidad de Carga", figsize=(13, 8), facecolor="white", edgecolor="blue"
)
p0 = 1
z = base64.decodestring("QXV0b3IgTmljb2xhcyBEYXZpZCBQYXN0cmFuIFphbW9yYQ==")
r1 = np.arange(0.0, 20.0, 0.005)
p1 = p0 * (1 - (r1 ** 2) / (20 ** 2))
plt.plot(r1, p1, color="#333FFF", linewidth=2)
plt.hold("true")

r2 = np.arange(0.0, 15.0, 0.005)
p2 = p0 * (1 - (r2 ** 2) / (15 ** 2))
plt.plot(r2, p2, "r", color="#339FFF", linewidth=2)
plt.hold("true")

r3 = np.arange(0.0, 10.0, 0.005)
p3 = p0 * (1 - (r3 ** 2) / (10 ** 2))
plt.plot(r3, p3, color="#3352FF", linewidth=2)
plt.hold("true")

r4 = np.arange(0.0, 5.0, 0.005)
p4 = p0 * (1 - (r4 ** 2) / (5 ** 2))
plt.plot(r4, p4, color="#337DFF", linewidth=2)
plt.hold("true")
plt.grid(color="0.5", linestyle="--", linewidth=1)
plt.title("$Densidad$ $de$ $carga$ $de$ $una$ $esfera$", fontsize=20, color="blue")
plt.ylabel("$Densidad$ $de$ $carga$ $(c/m^3)$", fontsize=16, color="blue")
plt.xlabel("$Radio (m)$", fontsize=16, color="blue")
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

plt.show()
