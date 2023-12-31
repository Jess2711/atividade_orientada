from abc import ABC
from iformato import IFormato
from ibolo import IBolo

#classe abstrata que implemanta a interface IBolo e é superclasse das classe boloSimples e Torta
class Bolo(ABC): 
    cont=0
    def __init__(self, custo: float , formato: IFormato = None):
        self._codigo = __class__.gera_codigo()
        self._custo = custo
        self._formato = formato
        IBolo.register(Bolo)
        

    #isinstance metodo para reconhecer o objeto, se for uma instancia de Bolo e tiver o msm codigo retornará true se não false
    def equals(self, obj):  
        if (isinstance(obj, Bolo)):
            return self.codigo == obj.codigo
        return False
    
    #método do contrato implementado na subclasses de Bolo
    def preco(self):
        pass
    #método que será implementado pelo resto da equipe
    def area(self):
        return 3 #retornei 3 apenas para testar o código
    
    #método de classe para gerar o código do bolo
    @classmethod
    def gera_codigo(cls):
        cls.cont+=1
        return str(cls.cont)

    
    #metodos acessadores e modificadores:
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

    #imprime as informações do bolo
    def __str__(self) -> str:
        return f'Código: {self.codigo}\nCusto: {self.custo}\nFormato do Bolo: {self.formato}'
    

    