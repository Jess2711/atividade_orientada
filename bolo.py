from abc import ABC
from formato import IFormato
from ibolo import IBolo

class Bolo(IBolo, ABC): #classe abstrata. E só tem metodos concretos?
    def __init__(self, codigo: int, custo: float, formato: IFormato = None):
        self._codigo = codigo 
        self._custo = custo
        self._formato = formato
    
    def preco(self) -> float:  #esse metodo está definido na Ibolo
        pass
    
    def area(self) -> float:
        return 40 #retornei um bvalor qualquer para testar 

    @property
    def codigo(self) -> int:
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor


    @property
    def custo(self) -> float:
        return self._custo
    
    @custo.setter
    def custo(self, valor):
        self._custo = valor

    @property
    def formato(self) -> IFormato:
        return self._formato
    
    @formato.setter
    def formato(self, valor):
        self._formato = valor

    def __str__(self) -> str:
        return f'custo: n\ {self.custo} codigo: n\ {self.codigo} formato: n\ {self.formato}'
    

    