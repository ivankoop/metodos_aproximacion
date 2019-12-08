
# Autor: Victor ivan koop Mendez
# Matricula: Co6219
# Profesor: Christian Mendoza Gomez

import math

def metodo_punto_fijo(f, p, TOL):
    error = 1
    iteraciones = 0
    while error > TOL:
        try:
            p_nuevo = f(p)
            error = abs(p_nuevo - p)
            p = p_nuevo
            iteraciones += 1
            print("Iteraciones:", iteraciones, "Punto: ", p, "Error: ", error)
        except OverflowError as error:
            print("Error con decimales")
            break
        if iteraciones > 1000:
            print("Demasiadas iteraciones necesarias")
            break
           
    print("Ultimo punto: ", p)

# Funcion: f(x) = 1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5)
# Toleracia 10^{-4}
def ejercicio1():

    def raiz(x):
        return(1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5))

    metodo_punto_fijo(raiz, 1, 10e-4)


# Funcion: f(x) = x**3-(2*math.sin(x))
# Toleracia 10^{-4}
def ejercicio2():

    def raiz(x):
        return(x**3-(2*math.sin(x)))

    metodo_punto_fijo(raiz, 1, 10e-4)


ejercicio1()