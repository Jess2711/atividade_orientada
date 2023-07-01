from bolo import Bolo
from iformato import IFormato

#classe concreta que herda de da classe Bolo, o bolo simples pode ser prozuzido sem lactose, o padrão é com lactose
class BoloSimples(Bolo):
    def __init__(self, custo: float, semLactose: bool = False,  formato: IFormato = None): 
        super().__init__(custo , formato)
        self._semLactose = semLactose
    
    #metodos acessadores e modificadores:
    @property
    def semLactose(self):
        return self._semLactose
    
    @semLactose.setter
    def semLactose(self, valor):
        self._semLactose = valor
 
    #implementação do metodo da interface Ibolo, o valor adicional foi armazenado em uma variavel e se caso semLactose seja true
    #esse valor é somado ao custo do bolo padrão
    def preco(self):      
        if self.semLactose == True:
            adicional = 35
            self.preco_bolo = self.custo*self.area() + adicional
            return self.preco_bolo
        else:
            self.preco_bolo = self.custo*self.area()
            return self.preco_bolo
     
    #imprime as informações do Bolo da super classe acrescido das informações do Bolo Simples
    def __str__(self) -> str:
        return f'Tipo do Bolo: Bolo Simples\n' + super().__str__() + f'\nLactose: {self.semLactose}\nPreço do Bolo informado: {self.preco_bolo}'