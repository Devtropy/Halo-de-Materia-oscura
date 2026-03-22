from funciones_fisicas import *
from metodos_numericos import *
from parametros import *
import matplotlib.pyplot as plt
import numpy as np
from graficadores import *
from mpl_toolkits.mplot3d import Axes3D
import time

t1 = time.time()
"================================ Condiciones iniciales ======================================="
R_s, M_s = particulas_con_simpson(n // 100)
R, M = particulas_con_biseccion(n, M_s, R_s)
error = error_porcentual(R, M, Masa_acumulada)
posiciones, velocidades, rpidez, vc, ve = condiciones_iniciales(R)

if max(rpidez) > 0.95 * max(ve):
    print("No se cumplio la condicion de ligadura")
    print(max(rpidez))
"================================== Graficas =================================================="
grafica_2D(
    posiciones[:, 0],
    posiciones[:, 1],
    "x (kpc)",
    "y (kpc)",
    "purple",
    " Proyeccion 2D del Halo",
    "Halo2D",
)
grafica_2D(R, ve, "R(kpc)", "Ve(kpc/Gyrs)", "blue", "ve vs r", "ve_vs_r")
grafica_2D(R, vc, "R(kpc)", "Vc(kpc/Gyrs)", "pink", "vc vs r", "vc_vs_r")
grafica_2D(R, M, "R(kpc)", "M(Masas solares)", "pink", "M vs r", "M_vs_r")
grafica_log(
    R,
    error,
    "R(kpc)",
    "Error porcentual",
    "red",
    "Error porcentual vs R",
    "grafica_error",
)
histograma(
    rpidez,
    "Rapidez(kpc/Gys)",
    "Frecuencia",
    "purple",
    "Distribucion de rapidez",
    "rapidez",
)
histograma_velocidad(
    velocidades[:, 0],
    "Rapidez en x(kpc/Gys)",
    "Frecuencia",
    "purple",
    "Distribucion de rapidez en x",
    "rapidezx",
)
histograma_velocidad(
    velocidades[:, 1],
    "Rapidez en y(kpc/Gys)",
    "Frecuencia",
    "purple",
    "Distribucion de rapidez en y",
    "rapidezy",
)
histograma_velocidad(
    velocidades[:, 2],
    "Rapidez en z(kpc/Gys)",
    "Frecuencia",
    "purple",
    "Distribucion de rapidez en z",
    "rapidezz",
)

"================================= Graficas 3D================================================="

fig = plt.figure(figsize=(10, 10))
fig.patch.set_facecolor("black")
ax = fig.add_subplot(projection="3d")
ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
ax.set_facecolor("black")
ax.scatter(
    posiciones[:, 0],
    posiciones[:, 1],
    posiciones[:, 2],
    c=posiciones[:, 2],
    cmap="viridis",
    marker="o",
    s=1,
)
ax.set_xlabel("X (kpc)", color="white")
ax.set_ylabel("Y (kpc)", color="white")
ax.set_zlabel("Z (kpc)", color="white")
ax.set_title("Halo de materia oscura", color="white")
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")
ax.tick_params(axis="z", colors="white")
ax.xaxis.line.set_color("white")
ax.yaxis.line.set_color("white")
ax.zaxis.line.set_color("white")
ax.grid(False)
plt.savefig("Halo.png")

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection="3d")
ax.scatter(
    posiciones[:, 0],
    posiciones[:, 1],
    posiciones[:, 2],
    c=posiciones[:, 2],
    cmap="viridis",
    marker="o",
)
ax.set_xlabel("X (kpc)")
ax.set_ylabel("Y (kpc)")
ax.set_zlabel("Z (kpc)")
ax.set_title("Halo de materia oscura")
plt.savefig("Halo_de_materia_oscura.png")
t2 = time.time()
print(f"Tiempo de ejecucion:{t2 - t1}")
