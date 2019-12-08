
# Autor: Victor ivan koop Mendez
# Matricula: Co6219
# Profesor: Christian Mendoza Gomez

import math

def metodo_newton_raphson(f, df, x, TOL):
    error = 1
    iteraciones = 0
    while error > TOL:
        p_nuevo = x - f(x)/df(x)
        error = abs(p_nuevo - x)
        x = p_nuevo
        iteraciones += 1
        print("Iteraciones:", iteraciones, "Punto: ", x, "Error: ", error)
    print("Ultimo punto: ", x)


# Funcion: f(x) = 1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5)
# Derivada f'(x) = 3*x**2-2*math.cos(x)
# Toleracia 10^{-4}
def ejercicio1():

    def f(x):
        return(1 - (3*x**2)*(math.exp(1)**-x) + (2*x**3)*math.sin(x)*math.exp(1)**(-x/5))

    def fprima(x):
        # muy dificil reemplazar la dervidada a condigo fuente, la funcion se cumple para el ej2
        return(1/5*math.exp(1)**(-x)*x*((10*(math.exp(1)**((4*x)/5)))*x**2*(math.cos(x))+(15*(x - 2)) - 2*math.exp(1)**((4*x)/5)*(x - 15)*x*math.sin(x)))


    metodo_newton_raphson(f, fprima, 2, 10e-4)

# Funcion: f(x) = x**3-(2*math.sin(x))
# Derivada f'(x) = 3*x**2-2*math.cos(x)
# Toleracia 10^{-4}
def ejercicio2():

    def f(x):
        return(x**3-(2*math.sin(x)))

    def fprima(x):
        return(3*x**2-2*math.cos(x))


    metodo_newton_raphson(f, fprima, 1, 10e-4)


ejercicio2()