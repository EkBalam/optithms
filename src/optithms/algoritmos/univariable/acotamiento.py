from typing import Callable
import numpy as np
from optithms.functions import Problema
from optithms.algoritmos.algoritmo import Algoritmo

class BusquedaExhaustiva(Algoritmo):
    """Algoritmo de búsqueda exhaustiva

    Args:
        Algoritmo (_type_): Algoritmo de búsqueda exhaustiva
    """

    def __init__(self, funcion: Callable, n: int, a: float = None, b: float = None) -> None:
        """_summary_

        Args:
            funcion (Callable): función a minimizar, debe ser univariable y retornar un valor flotante
            n (int): número de puntos intermedios
            a (float, optional): límite superior de la función a minimizar. Defaults to None.
            b (float, optional): límite inferior de la función a minimizar. Defaults to None.
        """
        super().__init__()
        self._funcion = funcion
        self.n, self.a, self.b = n, a, b
        if isinstance(self._funcion, Problema) :
            self.a, self.b = self._funcion.limites()

    def ejecutar(self)-> tuple[float, float]:
        """Ejecuta el algoritmo de búsqueda exhaustiva
        Returns:
            tuple[float, float]: intervalo donde se encuentra el mínimo
        """
        x1 = self.a
        delta_x = (self.b-self.a)/self.n
        x2 = x1 + delta_x
        x3 = x2 + delta_x
        while not (self._funcion(x1) >= self._funcion(x2) <= self._funcion(x3)) :
            x1, x2 = x2, x3
            x3 = x2 + delta_x
            if x3 > self.b:
                break
        return x1, x3

    @property
    def nombre(self):
        return "Busqueda Exhaustiva"


class FaseDeAcotamiento(Algoritmo):
    """Algoritmo de fase de acotamiento

    Args:
        Algoritmo (_type_): Algoritmo de fase de acotamiento
    """

    def __init__(self, funcion: Callable, x: float, delta: float) -> None:
        """_summary_

        Args:
            funcion (Callable): función a minimizar, debe ser univariable y retornar un valor flotante
            x (float): punto inicial
            delta (float): incremento (positivo)
        """
        super().__init__()
        self._funcion = funcion
        self.x = x
        self.delta = delta

    def ejecutar(self)-> tuple[float, float]:
        """Ejecuta el algoritmo de fase de acotamiento
        Returns:
            tuple[float, float]: intervalo donde se encuentra el mínimo
        """
        if self._funcion( self.x - np.abs(self.delta)) <= \
            self._funcion(self.x) <= self._funcion(self.x+np.abs(self.delta)) :
            self.delta *= -1
    
        k = 0
        x_k_menos1 = self.x
        x_k = self.x
        x_k_mas1 = x_k + (2**k) * self.delta

        while self._funcion(x_k_mas1) < self._funcion(x_k):
            x_k_menos1 = x_k
            x_k = x_k_mas1
            k += 1
            x_k_mas1 = x_k + (2**k) * self.delta
            
        return x_k_menos1, x_k_mas1
    
    @property
    def nombre(self):
        return "Busqueda de Fase de Acotamiento"

def acotamiento_fase(funcion, x: float, delta: float)-> tuple[float, float]:
    """Algoritmo de fase de acotamiento

    Args:
        funcion (_type_): 
        x (float): 
        delta (float): 

    Returns:
        tuple[float, float]: intervalo donde se encuentra el mínimo
    """
    if funcion( x - np.abs(delta)) <= funcion(x) <= funcion(x+np.abs(delta)) :
        delta *= -1
    
    k = 0
    x_k_menos1 = x
    x_k = x
    x_k_mas1 = x_k + (2**k) * delta
    
    while funcion(x_k_mas1) < funcion(x_k):
        x_k_menos1 = x_k
        x_k = x_k_mas1
        k += 1
        x_k_mas1 = x_k + (2**k) * delta
        
    return x_k_menos1, x_k_mas1
