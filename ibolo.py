from abc import ABC, abstractmethod

class IBolo(ABC):

    @abstractmethod
    def preco(self) -> float:
        pass #implementar o calculo de venda do bolo custo*área do bolo(quadrado, retangular, circular etc)