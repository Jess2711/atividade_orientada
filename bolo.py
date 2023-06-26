from abc import ABC
from iformato import IFormato
from ibolo import IBolo

class Bolo(ABC): #classe abstrata que implemanta a interface IBolo
    def __init__(self, codigo: int, custo: float , formato: IFormato = None):
        self._codigo = codigo 
        self._custo = custo
        self._formato = formato
        IBolo.register(Bolo)
        

    #isinstance metodo para reconhecer o objeto, se for uma instancia de Bolo e tiver o msm codigo retornará true se não false
    def equals(self, obj):  
        if (isinstance(obj, Bolo)):
            return self.codigo == obj.codigo
        return False
    
    #metodo do contrato
    def preco(self):
        pass

    def area(self):
        return 3 #retornei 3 para teste
    
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
        return f'Código: {self.codigo}\nCusto: {self.custo}\nFormato do Bolo: {self.formato}'
    

    