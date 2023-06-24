from abc import ABC, abstractmethod

class IFormato(ABC):

    @abstractmethod
    def area(self) -> float:
        return 5  # define a área do bolo(quadrado, retangular, circular etc) o 5 foi para testar