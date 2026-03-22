import matplotlib.pyplot as plt
import numpy as np

def grafica_2D(A,B,xlabel,ylabel,colors,title,nombre):
    plt.figure(figsize=(8,8))
    plt.scatter(A,B,color=colors,lw=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(nombre)

def grafica_log(A,B,xlabel,ylabel,colors,title,nombre):
    plt.figure(figsize=(8,8))
    plt.scatter(A,B,color=colors,lw=0.4)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(1e-13,1e-11)
    plt.title(title)
    plt.savefig(nombre)

def histograma(V,xlabel,ylabel,colors,title,nombre):

    frecuencias,espacio= np.histogram(V, bins=200, range=(0,np.max(V)))
    
    m =(espacio[:-1] + espacio[1:])/2
    
    plt.figure(figsize=(10, 6))
    plt.plot(m, frecuencias, color=colors, lw=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.savefig(nombre)

def histograma_velocidad(V, xlabel, ylabel, colors, title, nombre):
    V_max = np.max(np.abs(V))
    frecuencias, espacio = np.histogram(V, bins=200, range=(-V_max, V_max))
    
    m =(espacio[:-1] + espacio[1:])/2
    plt.figure(figsize=(10, 6))
    plt.plot(m, frecuencias, color=colors, lw=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.savefig(nombre)
 
 
