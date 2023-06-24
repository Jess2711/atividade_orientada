from abc import ABC, abstractmethod
from ibolo import IBolo

class IPrateleira(ABC): #esta faltando outros os demais metodos

    @abstractmethod
    def buscar(self) -> int: #buscar(IBolo)
        pass

    @abstractmethod
    def cheia(self) -> bool:
        pass
    
    @abstractmethod
    def vazia(self) -> bool:
        pass
    
    @abstractmethod
    def existe(self) -> bool: #existe(IBolo)
        pass
    
    @abstractmethod
    def inserir(self) -> bool: #inserir(IBolo)
        pass

    @abstractmethod
    def remover(self) -> IBolo: #remover(IBolo)
        pass

    @abstractmethod
    def remover(self) -> int: #remover(int)
        pass

    @abstractmethod
    def consultar(self) -> IBolo: #consultar(IBolo)
        pass

    @abstractmethod
    def listar(self) -> IBolo: #IBolo[]
        pass

    @abstractmethod
    def listar(self) -> str: #IBolo[]
        pass