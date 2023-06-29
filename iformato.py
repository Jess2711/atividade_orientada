from abc import ABC, abstractmethod

class IFormato(ABC):
# metodo que será definido pelo restante da equipe
    @abstractmethod
    def area(self) -> float:
        pass  # define a área do bolo(quadrado, retangular, circular etc) o 3 foi para testar
    
