from bolo import Bolo
from iformato import IFormato

class BoloSimples(Bolo):
    def __init__(self, custo: float, semLactose: bool = False,  formato: IFormato = None): 
        super().__init__(custo , formato)
        self._semLactose = semLactose
    
    @property
    def semLactose(self):
        return self._semLactose
    
    @semLactose.setter
    def semLactose(self, valor):
        self._semLactose = valor
 
    #implementação do metodo da interface Ibolo
    def preco(self):      
        if self.semLactose == True:
            adicional = 35
            self.preco_bolo = self.custo*self.area() + adicional
            return self.preco_bolo
        else:
            self.preco_bolo = self.custo*self.area()
            return self.preco_bolo
     
    def __str__(self) -> str:
        return f'Tipo do Bolo: Bolo Simples\n' + super().__str__() + f'\nLactose: {self.semLactose}\nPreço do Bolo informado: {self.preco_bolo}'