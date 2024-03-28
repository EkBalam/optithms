from typing import Callable
from typing import Any
from abc import ABC, abstractmethod, abstractproperty


class Algoritmo(ABC):

    @abstractmethod
    def ejecutar(self)->Any:
        """
        Ejecuta el algoritmo con los parametros establecidos.

        Returns:
            Any: resultado del algoritmo
        """

    @abstractproperty
    def nombre(self):
        pass

    def __str__(self) -> str:
        return self.nombre