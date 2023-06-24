from bolo import Bolo
from formato import IFormato

class Torta(Bolo):
    def __init__(self, codigo: int, custo: float, recheio: bool, cobertura: bool, formato: IFormato = None):
        super().__init__(codigo, custo , formato)
        self._recheio = recheio
        self._cobertura = cobertura

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
    
    def preco(): # recheio e cobertura aumenta o preço = custo*area
        pass
     
    def __str__(self) -> str:
        return super().__str__()