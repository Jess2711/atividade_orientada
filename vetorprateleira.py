from typing import Type
from iprateleira import IPrateleira
from ibolo import IBolo


class VetorPrateleira():
    def __init__(self, qtdbolo: int ):
        self.lista_prateleira()
        self._qtdbolo = qtdbolo
        IPrateleira.register(VetorPrateleira)

    def bolo(self, obj):  
        if (isinstance(obj, IPrateleira)):
            obj.inserir()
            return True
        else:
            print('Não tem bolo')
            return False


    @property
    def qtdbolo(self):
        return self._qtdbolo
    
    @qtdbolo.setter
    def qtdbolo(self, valor):
        self._qtdbolo = valor
    
    def lista_prateleira(self): #prateleira_bolos: Type[IBolo]):  #instanciar e inicializar a lista de prateleira de tipo IBolo
        self.prateleira_bolos = [] #tamanho estabelecido pelo usuario
        print(self.prateleira_bolos)
        
    def inserir(self):    #O método deverá lançar uma mensagem “Bolo já cadastrado.” caso exista na prateleira pelo menos um bolo com o mesmo código. 
        novo_bolo = IBolo()
        self.prateleira_bolos.append(novo_bolo)
        print(novo_bolo)
        print(self.prateleira_bolos)
    
    def remover_bolo(self): #IBolo bolo
        pass
     
    def remover_posicao_bolo(self): #int posicaos
        pass
 
    def listar_tipo_bolo(self):
        pass

    #os metodos do contrato

    def buscar(self) -> int: #buscar(IBolo)
        pass

    def cheia(self) -> bool:
        pass
    
    def vazia(self) -> bool:
        pass
    
    def existe(self) -> bool: #existe(IBolo)
        pass
    
    def inserir(self) -> bool: #inserir(IBolo)
        pass

    def remover(self) -> IBolo: #remover(IBolo)
        pass

    def remover(self) -> int: #remover(int)
        pass

    def consultar(self) -> IBolo: #consultar(IBolo)
        pass

    def listar(self) -> IBolo: #IBolo[]
        pass

    def listar(self) -> str: #IBolo[]
        pass