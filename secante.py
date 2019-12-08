# Autor: Victor ivan koop Mendez
# Matricula: Co6219
# Profesor: Christian Mendoza Gomez

import math
import numpy as np
import matplotlib.pyplot as plt

def metodo_secante(f, x1, x2, TOL):
    error = 1
    iteraciones = 0
    while error > TOL:
        p_nuevo = x2 - (f(x2)*(x2-x1))/(f(x2)-f(x1))
        error = abs(p_nuevo - x2)
        x1 = x2
        x2 = p_nuevo
        iteraciones += 1
        print("Iteraciones:", iteraciones, "Punto1: ", x1 ,"Punto2: ", x2, "Error: ", error)
        yield iteraciones, abs(x1), abs(x2)
    print("Ultimo punto: ", x2)


# Funcion: f(x) = 1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5)
# Intervalo [4,20]
# Toleracia 10^{-4}
def ejercicio1():

    def raiz(x):
        return(1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5))

    data = np.array(list(metodo_secante(raiz, 4, 20, 10e-4)))
    plt.plot(data[:,0], data[:,1])
    plt.show()

# Funcion: f(x) = x**3-(2*math.sin(x))
# Intervalo [-5,5]
# Toleracia 10^{-4}
def ejercicio2():

    def raiz(x):
        return(x**3-(2*math.sin(x)))
    

    data = np.array(list(metodo_secante(raiz, -5, 5, 10e-4)))
    plt.plot(data[:,0], data[:,1])
    plt.show()

ejercicio1()