from optithms.functions import Problema
import numpy as np

class Lata(Problema):
    """ Función para calcular el area de una lata para contener 250ml de liquido. 
    Basado en el radio de la lata.
    """

    def funcion(self, r:list[float]) -> float:
        """_summary_

        Args:
            r (list[float]): _description_

        Returns:
            float: _description_
        """
        super().funcion(r)
        return 2 * np.pi * (r**2)

    def limites(self) -> tuple[float, float]:
        """
        Sus limites son: 
        (0, 10], 0 < radio <= 10

        Returns:
            tuple[float, float]: límite superior y límite inferior
        """        
        return 0.00001, 10.0


def caja(l:float) -> float:
    """
    Se quiere construir una caja sin tapa a partir de una hoja de cartón de 20x10cm. 
    Para ello, se corta un cuadrado de lado L en cada esquina y se dobla la hoja levantando 
    los cuatro laterales de la caja.
    
    Determinar las dimensiones de la caja para que su volumen sea máximo si el lado 
    L debe medir entre 2 y 3 cm ( 2 ≤ L ≤ 3 ).

    Args:
        alto (float): alto L de la caja

    Returns:
        float: Volumen de la cada dado un L
    """
    return (20 - 2 * l) * (10 - 2 * l) * (l)


class Funcion1(Problema):
    """
    .. math::
       f(x) = x^2+\frac{ 54  }{ x }
    """
    
    def funcion(self, x:list[float]) -> float:
        """.. math::
       f(x) = x^2+\frac{ 54  }{ x }

        Args:
            x (list[float]): variable independiente

        Returns:
            float: _description_
        """
        super().funcion(x)
        return (x**2) + (54/x)

    def limites(self) -> tuple[float, float]:
        """
        Sus limites son: 
        (0, 10], 0 < x <= 10

        Returns:
            tuple[float, float]: límite superior y límite inferior
        """
        return 0.00001, 10.0


def funcion1(x:float) -> float:
    """
    .. math::
       f(x) = x^2+\frac{ 54  }{ x }
    
    Sus limites son: 
        (0, 10], 0 < x <= 10

    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (x**2) + (54/x)


def funcion2(x:float) -> float:
    """
    .. math::
       f(x) = x^3 + x^2 - 3

    Sus limites son: 
     (0, 5], 0 < x <= 5
       
    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (x**3) + (2*x) - 3

# Valores entre -2.5 o igual a 2.5
def funcion3(x:float) -> float:
    """
    .. math::
       f(x) = x^4 + x^2 - 33

    Sus limites son: 
     [-2.5, 2.5], -2.5 < x <= 2.5
       
    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (x**4) + (x**2) - 33


def funcion4(x:float) -> float:
    """
    .. math::
       f(x) = 3x^4 - 8x^3 - 6x^2 + 12x

    Sus limites son: 
     [-1.5, 3], -1.5 < x <= 3
       
    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x)