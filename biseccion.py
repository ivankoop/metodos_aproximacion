
# Autor: Victor ivan koop Mendez
# Matricula: Co6219
# Profesor: Christian Mendoza Gomez

import numpy as np
import matplotlib.pyplot as plt

import math

def metodo_biseccion(f, a, b, tol):
    if f(a)*f(b) > 0:
        print("No se encontro la raiz")
    else:
        iter = 0
        while (b - a) / 2.0 > tol:
            punto_medio = (a + b) / 2.0
            print("Punto medio: ", punto_medio)
            yield iter, abs(f(punto_medio))
            if f(a) * f(punto_medio) < 0: # Aumentando pero menor a 0 
                b = punto_medio
            else:
                a = punto_medio
            iter += 1
    print("Iteraciones: ", iter)


# Funcion: f(x) = 1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5)
# Intervalo [4,20]
# Toleracia 10^{-4}
def ejercicio1():

    def raiz(x):
        return(1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5))

    data = np.array(list(metodo_biseccion(raiz, 4, 20, 10e-4)))
    plt.plot(data[:,0], data[:,1])
    plt.show()

# Funcion: f(x) = x**3-(2*math.sin(x))
# Intervalo [-5,5]
# Toleracia 10^{-4}
def ejercicio2():

    def raiz(x):
        return(x**3-(2*math.sin(x)))

    data = np.array(list(metodo_biseccion(raiz, -5, 5, 10e-4)))
    plt.plot(data[:,0], data[:,1])
    plt.show()

ejercicio2()
