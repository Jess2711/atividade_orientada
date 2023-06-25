from bolo import Bolo
from iformato import IFormato

class BoloSimples(Bolo):
    def __init__(self, codigo: int, custo: float,  formato: IFormato = None, semLactose: bool = None): #Pq dois construtores? não pode só colocar None se não passar nada é simples?
        super().__init__(codigo, custo , formato)
        self._semLactose = semLactose
    
    @property
    def semLactose(self):
        return self._semLactose
    
    @semLactose.setter
    def semLactose(self, valor):
        self._semLactose = valor

    def tipoBolo(self): #colocar o acrescimo de 35 reais aqui? 
        if self.semLactose == self.semLactose:
            return True
        else:
            return False 
    
    def preco(self):      #mano isso aqui vem da classe abstrata bolo ou da interface Ibolo?
        self.preco_bolo = self.custo*self.area()
        return self.preco_bolo
     
    def __str__(self) -> str:
        return super().__str__() + f'\nLactose: {self.semLactose}\nPreço do Bolo informado: {self.preco_bolo}'