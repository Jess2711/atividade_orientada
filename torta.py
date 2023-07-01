from bolo import Bolo
from iformato import IFormato

#classe concreta Torta que herda da classe Bolo, a Torta pode ser prozuzido com recheio, com cobertura
#ou com ambos, não existe Torta sem nenhum desses, pq logo seria bolo simples
class Torta(Bolo):
    def __init__(self, custo: float, recheio: bool = True, cobertura: bool = True, formato: IFormato = None):
        super().__init__(custo , formato)
        self._recheio = recheio
        self._cobertura = cobertura

    #metodos acessadores e modificadores:
    @property
    def recheio(self):
        return self._recheio
    
    @recheio.setter
    def recheio(self, valor):
        self._recheio = valor

    @property
    def cobertura(self):
        return self._cobertura
    
    @recheio.setter
    def cobertura(self, valor):
        self._cobertura = valor
    
    # metodo para calculo do preço que tem que ter pelo menos 1 acrecimo: recheio e/ou cobertura 
    # que aumenta o preço padrão mais o adicional
    def preco(self): 
        if self.recheio == False:
            adicional = 20.00
            self.preco_torta = self.custo*self.area() + adicional
            return self.preco_torta 
        elif self.cobertura == False:
            adicional = 12.50
            self.preco_torta = self.custo*self.area() + adicional
            return self.preco_torta 
        else:
            adicional = 32.50
            self.preco_torta = self.custo*self.area() + adicional
            return self.preco_torta 

     
    def __str__(self) -> str:
        return f'Tipo do Bolo: Torta\n' + super().__str__() + f'\nPreço da Torta: {self.preco_torta}'