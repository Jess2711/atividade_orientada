#from typing import Type
from prateleira import IPrateleira
from ibolo import IBolo


class VetorPrateleira(IPrateleira, IBolo):
    def __init__(self, qtdbolo: int ):
        self._prateleira = self.listar() #metodo da lista de bolos em prateleira
        self._qtdbolo = qtdbolo
    
    #def lista_prateleira(self, bolos: Type[IBolo]):
    def inserir(self):
        pass
    
    def remover(self): #int posicao
        pass

    def remover(self): #IBolo bolo
        pass
 
    def listar(self):
        pass