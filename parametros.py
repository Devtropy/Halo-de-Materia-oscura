import math

a = 21.6  # kpc
Masa_total = 10e12  # Masas solares
Radio_halo = 256  # kpc
n = 10000
rho_0 = (3 * Masa_total) / (
    8 * math.pi * a**3 * math.log((Radio_halo / a) ** (3 / 2) + 1)
)
G = 4.5143e-6
