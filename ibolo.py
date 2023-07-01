from abc import ABC, abstractmethod
#essa classe abstrata por convenção é uma interface os métodos definidos nela serão implementados, 
#quando necessário, na classe concreta que a implementar.
class IBolo(ABC): 
    @abstractmethod
    def preco(self) -> float:
        pass 