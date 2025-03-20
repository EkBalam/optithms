from typing import Callable
from optithms.algoritmos.algoritmo import Algoritmo
from optithms.functions.problema import Problema

def primera_derivada_numerica(funcion:Callable, x:float, delta:float=1e-6) -> float:
    return (funcion(x + delta) - funcion(x - delta)) / (2*delta)


def segunda_derivada_numerica(funcion:Callable, x:float, delta:float=1e-6) -> float:
    return  (funcion(x + delta) - (2*funcion(x)) + funcion(x - delta)) / (delta**2)


class NewtonRaphson(Algoritmo):
    
    def __init__(self, funcion:Callable, x:float, epsilon:float=1e-7) -> None:
        self._funcion = funcion
        self.epsilon = epsilon
        self.x = x

    def ejecutar(self) -> float:
        xt = self.x

        primera_derivada = primera_derivada_numerica(self._funcion, xt, self.epsilon)
        
        while abs(primera_derivada) > self.epsilon:
            segunda_derivada = segunda_derivada_numerica(self._funcion, xt, self.epsilon)
            xt = xt - primera_derivada/segunda_derivada
            primera_derivada = primera_derivada_numerica(self._funcion, xt, self.epsilon)
        
        return xt
    
    @property
    def nombre(self):
        return "Newton-Raphson"


class Biseccion(Algoritmo):
    
    def __init__(self, funcion:Callable, epsilon:float=1e-7, limite_inferior:float=None, 
                 limite_superior:float=None) -> None:
        self._funcion = funcion
        self.epsilon = epsilon
        self.epsilon, self.inferior, self.superior = epsilon, limite_inferior, limite_superior
        if isinstance(self._funcion, Problema) :
            self.a, self.b = self._funcion.limites()

    def ejecutar(self) -> float:
        
        x1, x2 = self.__calcular_puntos()

        z = (x2+x1)/2
        primera_derivada = primera_derivada_numerica(self._funcion, z, self.epsilon)
        
        while abs(primera_derivada) > self.epsilon:
            if primera_derivada < 0:
                x1 = z
            if primera_derivada > 0:
                x2 = z
            
            z = (x2+x1)/2
            primera_derivada = primera_derivada_numerica(self._funcion, z, self.epsilon)
        
        return z
    
    def __calcular_puntos(self):
        return self.inferior, self.superior

    @property
    def nombre(self):
        return "Biseccion"
    

class Secante(Algoritmo):
    
    def __init__(self, funcion:Callable, epsilon:float=1e-7, limite_inferior:float=None, 
                 limite_superior:float=None) -> None:
        self._funcion = funcion
        self.epsilon = epsilon
        self.epsilon, self.inferior, self.superior = epsilon, limite_inferior, limite_superior
        if isinstance(self._funcion, Problema) :
            self.a, self.b = self._funcion.limites()

    def ejecutar(self) -> float:
        
        x1, x2 = self.__calcular_puntos()
        
        primera_derivada_x1 = primera_derivada_numerica(self._funcion, x1, self.epsilon)
        primera_derivada_x2 = primera_derivada_numerica(self._funcion, x2, self.epsilon)
        z = x2 - ( primera_derivada_x2 / ((primera_derivada_x2-primera_derivada_x1)/(x2-x1)) )
        primera_derivada_z = primera_derivada_numerica(self._funcion, z, self.epsilon)

        while abs(primera_derivada_z) > self.epsilon:
            if primera_derivada_z < 0:
                x1 = z
            if primera_derivada_z > 0:
                x2 = z
            
            primera_derivada_x1 = primera_derivada_numerica(self._funcion, x1, self.epsilon)
            primera_derivada_x2 = primera_derivada_numerica(self._funcion, x2, self.epsilon)
            z = x2 - ( primera_derivada_x2 / ((primera_derivada_x2-primera_derivada_x1)/(x2-x1)) )
            primera_derivada_z = primera_derivada_numerica(self._funcion, z, self.epsilon)
            
        return z
    
    def __calcular_puntos(self):
        return self.inferior, self.superior

    @property
    def nombre(self):
        return "Secante"

