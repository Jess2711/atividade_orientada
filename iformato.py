from abc import ABC, abstractmethod
#essa classe abstrata por convenção é uma interface os métodos definidos nela serão implementados, 
#quando necessário, na classe concreta que a implementar.
class IFormato(ABC):
# metodo que será definido pelo restante da equipe
    @abstractmethod
    def area(self) -> float:
        pass  
    
