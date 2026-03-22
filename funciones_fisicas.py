from parametros import *
import math
import random
import numpy as np
import pandas as pd
from metodos_numericos import *


def perfil_de_densidad(r):
    return rho_0 / ((r / a) ** (3 / 2) * (1 + (r / a) ** (3 / 2)))


def Masa_acumulada(r):
    return (
        (math.log((r / a) ** (3 / 2) + 1))
        / (math.log((Radio_halo / a) ** (3 / 2) + 1))
        * Masa_total
    )


def particulas_con_biseccion(p, M, R):
    r_biseccion = []
    m_biseccion = []
    q = len(M)
    for i in range(1, p + 1):
        masa_aleatoria = random.uniform(0.0, Masa_total)
        indice = busqueda_binaria(masa_aleatoria, M)
        if indice <= 0:
            alpha = 0
            beta = 1
        elif indice >= q - 1:
            alpha = q - 2
            beta = q - 1
        else:
            alpha = indice - 1
            beta = indice + 1
        r = biseccion(
            lambda r: Masa_acumulada(r) - masa_aleatoria, R[alpha], R[beta], 1e-12, 1000
        )
        r_biseccion.append(r)
        m_biseccion.append(masa_aleatoria)
    return r_biseccion, m_biseccion


def particulas_con_simpson(o):
    h = Radio_halo / o
    M = []
    R = []
    R.append(1e-12)
    M.append(1e-12)
    for i in range(1, o + 1):
        r_i = i * h
        M_i = (
            4.0
            * math.pi
            * simpson13(lambda r: perfil_de_densidad(r) * r**2, 1e-6, r_i, 100000)
        )
        M.append(M_i)
        R.append(r_i)
    return R, M


def dispersion_radial(r):
    integral = simpson13(
        lambda x: G * perfil_de_densidad(x) * Masa_acumulada(x) / x**2,
        r,
        Radio_halo,
        1000,
    )
    dispersion = integral / perfil_de_densidad(r)
    return dispersion


def Henon(r):
    x1 = random.uniform(0, 1)
    x2 = random.uniform(0, 1)
    x3 = random.uniform(0, 1)
    x4 = random.uniform(0, 1)

    rapidez1 = math.sqrt(dispersion_radial(r) * -2 * math.log(1 - x1))
    theta1 = 2 * math.pi * x2
    rapidez2 = math.sqrt(dispersion_radial(r) * -2 * math.log(1 - x3))
    theta2 = 2 * math.pi * x4

    vx = rapidez1 * math.cos(theta1)
    vy = rapidez1 * math.sin(theta1)
    vz = rapidez2 * math.sin(theta2)

    return vx, vy, vz


def posicionamiento(r):
    z = random.uniform(-r, r)
    phi = random.uniform(0, 2 * math.pi)
    x = math.sqrt(r**2 - z**2) * math.cos(phi)
    y = math.sqrt(r**2 - z**2) * math.sin(phi)
    return x, y, z


def vc(r):
    return math.sqrt(G * Masa_acumulada(r) / r)


def ve(r):
    potencial = simpson13(lambda x: -G * Masa_acumulada(x) / x**2, r, Radio_halo, 1000)
    return math.sqrt(-2 * potencial)


def condiciones_iniciales(r):
    posiciones = np.zeros((n, 3))
    velocidades = np.zeros((n, 3))
    rapidez = []
    v_c = []
    v_e = []
    for i in range(0, n):
        posiciones[i, :] = posicionamiento(r[i])
        velocidades[i, :] = Henon(r[i])
        v = vc(r[i])
        v2 = ve(r[i])
        v_c.append(v)
        v_e.append(v2)
    for i in range(0, n):
        rp = 0.0
        for j in range(0, 3):
            rp += velocidades[i, j] ** 2
        rp = math.sqrt(rp)
        rapidez.append(rp)

    pos = pd.DataFrame(
        {"x": posiciones[:, 0], "y": posiciones[:, 1], "z": posiciones[:, 2]}
    )
    vel = pd.DataFrame(
        {"vx": velocidades[:, 0], "vy": velocidades[:, 1], "vz": velocidades[:, 2]}
    )

    pos.to_csv("posiciones.csv")
    vel.to_csv("velocidades.csv")

    return posiciones, velocidades, rapidez, v_c, v_e
