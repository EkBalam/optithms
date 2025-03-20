import math
from optithms.functions import Lata, Funcion1, Caja
from optithms.algoritmos.univariable import BusquedaExhaustiva, FaseDeAcotamiento
from optithms.algoritmos.univariable import IntervalosMitad, Fibonacci, BusquedaDorada
from optithms.algoritmos.univariable import NewtonRaphson


def n_fibonacci(n):
    PHI = ( 1 + math.sqrt(5) ) / 2
    return int((PHI**n - (1-PHI)**n)/ math.sqrt(5))

if __name__ == "__main__":

    # fa = FaseDeAcotamiento(Caja(), 2.1, 0.001)
    # print(f"{fa} Clase callable ", fa.ejecutar())


    # be = BusquedaExhaustiva(Funcion1(), 10)

    # print(f"{be} Clase callable ", be.ejecutar())

    # fa = FaseDeAcotamiento(Funcion1(), 0.6, 0.5)
    # print(f"{fa} Clase callable ", fa.ejecutar())

    # im = IntervalosMitad(Funcion1(), epsilon=10e-3)
    # print(f"{im} Clase callable ", im.ejecutar())

    # fib = Fibonacci(Funcion1(), n=15)
    # print(f"{fib} Clase callable ", fib.ejecutar())

    # bd = BusquedaDorada(Funcion1(), epsilon=10e-3)
    # print(f"{bd} Clase callable ", bd.ejecutar())

    # new = NewtonRaphson(Funcion1(), 0.6)
    # print(f"{new} Clase callable ", new.ejecutar())
    
    # for n in range(6, -1, -1):
    #     print(n, n_fibonacci(n))
    
    f = lambda x: x**2 - x**4
    im = IntervalosMitad( f, epsilon=0.1, a=-0.6, b=0.6)
    print(f"{im} Clase callable ", im.ejecutar())


    fib = Fibonacci(f, n=10,  a=-0.6, b=0.6)
    print(f"{fib} Clase callable ", fib.ejecutar())