from formato import IFormato
from ibolo import IBolo

class Bolo(IFormato, IBolo): #classe abstrata
    def __init__(self, custo: float, formato: IFormato):
        self._codigo = __class__.geracodigo() #o codigo não é randomico ? “Bolo já cadastrado.” caso
#exista na prateleira pelo menos um bolo com o mesmo código.
        self._custo = custo
        self._formato = formato

    @property
    def codigo(self) -> int:
        return self._custo
    
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
        return self._custo
    
    @formato.setter
    def formato(self, valor):
        self._formato = valor

    def __str__(self) -> str:
        return f'custo: n\ {self.custo} codigo: n\ {self.codigo} formato: n\ {self.formato}'
    

    