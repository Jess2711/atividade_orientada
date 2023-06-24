from abc import ABC, abstractmethod
from ibolo import IBolo

class IPrateleira(ABC):

    @abstractmethod
    def buscar(self) -> int:
        pass

    @abstractmethod
    def cheia(self) -> bool:
        return True
    
    @abstractmethod
    def vazia(self) -> bool:
        return True

    @abstractmethod
    def listar(self):
        self.lista_bolos = []
        