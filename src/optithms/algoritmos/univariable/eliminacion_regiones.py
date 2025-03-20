import math
from typing import Callable
from optithms.algoritmos.algoritmo import Algoritmo
from optithms.functions.problema import Problema


class IntervalosMitad(Algoritmo):
    
    def __init__(self, funcion:Callable, epsilon:float, a:float=None, b:float=None) -> None:
        self._funcion = funcion
        self.epsilon, self.a, self.b = epsilon, a, b
        if isinstance(self._funcion, Problema) :
            self.a, self.b = self._funcion.limites()

    def ejecutar(self) -> float:
        a, b = self.a, self.b
        L = b - a
        xm = (a + b)/2

        while L > self.epsilon:
            x1 = a + L/4
            x2 = b - L/4
            print(x1, xm, x2)

            fxm = self._funcion(xm)
            if self._funcion(x1) < fxm:
                b, xm = xm, x1
            elif self._funcion(x2) < fxm:
                a, xm = xm, x2
            else:
                a, b = x1, x2
            
            L = b - a
        
        return a, b
    
    @property
    def nombre(self):
        return "Intervalos por la mitad"


def regla_eliminacion(x1, x2, fx1, fx2, a, b)->tuple[float, float]:
    if fx1 > fx2:
        return x1, b

    if fx1 < fx2:
        return a, x2
    
    return x1, x2


class Fibonacci(Algoritmo):

    PHI = ( 1 + math.sqrt(5) ) / 2
    
    def __init__(self, funcion:Callable, n:int, a:float=None, b:float=None) -> None:
        self._funcion = funcion
        self.n, self.a, self.b = n, a, b
        if isinstance(self._funcion, Problema) :
            self.a, self.b = self._funcion.limites()

    def ejecutar(self) -> float:
        k = 2
        a, b = self.a, self.b
        L = b - a
        fib_n1 = self.n_fibonacci(self.n+2)        

        while k <= self.n:
            Lk = (self.n_fibonacci(self.n-k+2)/fib_n1)*L
            
            x2 = a + Lk
            x1 = b - Lk
            print(x1, x2)

            a, b = regla_eliminacion(x1, x2, self._funcion(x1), self._funcion(x2), a, b)
            
            k+=1

        return a, b

    def n_fibonacci(self, n:int) -> int:
        return int((Fibonacci.PHI**n - (1-Fibonacci.PHI)**n)/ math.sqrt(5))

    @property
    def nombre(self):
        return "Metodo de Fibonacci"
    
class BusquedaDorada(Algoritmo):

    PHI = ( 1 + math.sqrt(5) ) / 2 - 1
    
    def __init__(self, funcion:Callable, epsilon:float, a:float=None, b:float=None) -> None:
        self._funcion = funcion
        self.epsilon, self.a, self.b = epsilon, a, b
        if isinstance(self._funcion, Problema) :
            self.a, self.b = self._funcion.limites()

    def w_to_x(self, w:float) -> float:
        return w * (self.b-self.a) + self.a

    def ejecutar(self) -> float:
        aw, bw = 0, 1
        Lw = 1
        k = 1
        
        while Lw > self.epsilon:
            w2 = aw + BusquedaDorada.PHI*Lw
            w1 = bw - BusquedaDorada.PHI*Lw
            aw, bw = regla_eliminacion(w1, w2, self._funcion(self.w_to_x(w1)), 
                                     self._funcion(self.w_to_x(w2)), aw, bw)
            k+=1
            Lw = bw - aw

        return self.w_to_x(aw), self.w_to_x(bw)

    @property
    def nombre(self):
        return "Busqueda Dorada"
