from abc import ABC, abstractmethod

class IFormato(ABC):

    @abstractmethod
    def area(self) -> float:
        return 3  # define a área do bolo(quadrado, retangular, circular etc) o 3 foi para testar
    
