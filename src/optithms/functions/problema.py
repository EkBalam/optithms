from abc import ABC, abstractmethod
from typing import Any


class Problema(ABC):

    @abstractmethod
    def funcion(self, x:list[float]) -> float:
        if x < self.limites()[0] or x > self.limites()[1]:
            raise ValueError(f"Variable fuera de los limites x: {x}, " + 
                             f"li: {self.limites()[0]}, ls: {self.limites()[1]}")

    @abstractmethod
    def limites(self) -> tuple[float, float]:
        pass

    def __call__(self, x:list[float]) -> Any:
        return self.funcion(x)