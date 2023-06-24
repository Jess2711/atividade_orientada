from abc import ABC, abstractmethod

class IFormato(ABC):

    @abstractmethod
    def area(self) -> float:
        pass  # define a área do bolo(quadrado, retangular, circular etc)