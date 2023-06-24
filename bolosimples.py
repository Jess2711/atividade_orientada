from bolo import Bolo

class BoloSimples(Bolo):
    def __init__(self, custo: float, semLactose: bool):
        super().__init__(custo)
        self._semLactose = semLactose
    
    @property
    def semLactose(self):
        return self._semLactose
    
    @semLactose.setter
    def semLactose(self, valor):
        self._semLactose = valor

    
    def preco():
        pass
     
    def __str__(self) -> str:
        return super().__str__()