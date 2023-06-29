#from typing import list
from iprateleira import IPrateleira
from ibolo import IBolo
from bolosimples import BoloSimples
from bolo import Bolo


class VetorPrateleira():
    def __init__(self, tamanho: int):
        self.prateleira_bolos:IBolo = []
        self._tamanho = tamanho
        IPrateleira.register(VetorPrateleira)

    def bolo(self, obj):  
        if (isinstance(obj, IPrateleira)):
            obj.inserir()
            return True
        else:
            print('Não tem bolo')
            return False


    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, valor):
        self._tamanho = valor

    def equals(self, obj):  
        if (isinstance(obj, Bolo)):
            return self.codigo == obj.codigo
        return False    
    
        
    def inserir(self, bolo: IBolo) -> bool:    #O método deverá lançar uma mensagem “Bolo já cadastrado.” caso exista na prateleira pelo menos um bolo com o mesmo código. 
        #if (isinstance(obj_bolo, IBolo)):
        for obj_bolo in self.prateleira_bolos:  #percorrer a lista de bolos dentro de for jogar o equals, já existe o bolo
            if obj_bolo.codigo == bolo.codigo:
                print('Bolo já cadastrado')
                return
        if len(self.prateleira_bolos) < self.tamanho:
            self.prateleira_bolos.append(bolo)
            print('Bolo inserido')
        else:
            print('Prateleira cheia')
        print(self.prateleira_bolos)
        #print(type(self.prateleira_bolos))
    

        #self.prateleira_bolos.append(novo_bolo)
        #print(novo_bolo)
        #print(self.prateleira_bolos)
    
    def remover(self, bolo) -> IBolo: #IBolo bolo
        if bolo in self.prateleira_bolos:
            self.prateleira_bolos.remove(bolo)
            print('bolo', bolo, 'removido')
        else: 
            print('Bolo inexistente')

    def remover_posicao(self, posicao) -> int: #IBolo bolo
        if self.prateleira_bolos[posicao] in self.prateleira_bolos:
            del self.prateleira_bolos[posicao]
            print('bolo removido da posição:', posicao)
        else: 
            print('Bolo inexistente')

    '''
    def remover(self, posicao) -> int: #int posicao
        for obj_bolo in self.prateleira_bolos:
            if self.prateleira_bolos(obj_bolo):
                del self.prateleira_bolos[posicao]
                print(posicao)
            else: 
                print('Bolo inexistente')
    '''

 
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
    
    #def inserir(self) -> bool: #inserir(IBolo)
        #pass

    #def remover(self) -> IBolo: #remover(IBolo)
        pass

    #def remover(self) -> int: #remover(int)
        pass

    def consultar(self) -> IBolo: #consultar(IBolo)
        pass

    def listar(self) -> IBolo: #IBolo[]
        pass

    def listar(self) -> str: #IBolo[]
        pass