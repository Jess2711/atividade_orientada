from bolo import Bolo

class Torta(Bolo):
    def __init__(self, custo: float, recheio: bool, cobertura: bool):
        super().__init__(custo)
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
    
    def preco():
        pass
     
    def __str__(self) -> str:
        return super().__str__()