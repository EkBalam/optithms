from typing import Any, Callable
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

            fxm = self._funcion(xm)
            if self._funcion(x1) < fxm:
                b, xm = xm, x1
            elif self._funcion(x2) < fxm:
                a, xm = xm, x2
            else:
                a, b = x1, x2
            
            L = b - a
        
        return xm
    
    @property
    def nombre(self):
        return "Intervalos por la mitad"
