#from typing import list
from iprateleira import IPrateleira
from ibolo import IBolo
from bolosimples import BoloSimples
from bolo import Bolo
from torta import Torta


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

    #essa função trouxe da classe bolo para tentar fazer funcionar na função inserir
    '''
    def equals(self, obj):  
        if (isinstance(obj, Bolo)):
           return self.codigo == obj.codigo
        return False 
    '''   
    
    #O método deverá lançar uma mensagem “Bolo já cadastrado.” caso exista na prateleira pelo menos um bolo com o mesmo código, método da interface.    
    def inserir(self, bolo: IBolo) -> bool:  
        #percorrer a lista de bolos dentro de for (não deu certo com a função equals, se já existe não insere)
        for obj_bolo in self.prateleira_bolos:  
            if obj_bolo.codigo == bolo.codigo:
                print('Bolo já cadastrado')
                return
        if len(self.prateleira_bolos) < self.tamanho:
            self.prateleira_bolos.append(bolo)
            print('Bolo inserido')
        else:
            print('Prateleira cheia')
        print(self.prateleira_bolos)
        
    def remover(self, bolo) -> IBolo: #IBolo bolo
        if bolo in self.prateleira_bolos:
            self.prateleira_bolos.remove(bolo)
            print('bolo', bolo, 'removido')
        else: 
            print('Bolo inexistente')

    def remover_posicao(self, posicao) -> int: #IBolo bolo
        if posicao<len(self.prateleira_bolos) and self.prateleira_bolos[posicao] in self.prateleira_bolos:
            del self.prateleira_bolos[posicao]
            print('bolo removido da posição:', posicao)
        else: 
            print('Bolo inexistente')
    '''
    Codificar o método listar(char tipoDoBolo) responsável por retornar uma lista de
    bolos do tipo especificado. Caso o tipoDoBolo seja “S”, a lista deverá conter apenas
    exemplares de bolos do tipo BoloSimples. Caso o tipoDoBolo seja “T”, a lista deverá
    conter apenas exemplares de bolos do tipo Torta.
    '''
    
    #Jéssica
    def listar_tipo_bolo(self, tipo:str):
        lista_tipo = []
        if tipo == 'S':
            for bolo in self.prateleira_bolos:  
                if (isinstance(bolo, BoloSimples)):
                    lista_tipo.append(bolo)
                    #print(lista_tipo)
        elif tipo == 'T':
            for bolo in self.prateleira_bolos:  
                if (isinstance(bolo, Torta)):
                    lista_tipo.append(bolo)
                    #print(lista_tipo)
        else:
            return 'Digite um tipo existente'
        return lista_tipo

    

    '''     
    def listar(self, tipo_bolo):
        torta = []
        bolo_simples = []
        for valor in (self.prateleira_bolos):
            if (isinstance(valor, Torta)): #Alterar para reconhecer o objeto
                torta.append(valor)
            else:
                bolo_simples.append(valor)
        if tipo_bolo.upper() == 'T':
            return torta
        return bolo_simples
    '''
            

        
    '''
        lista_tipo = []
        if tipoBolo == 'S':
            lista_tipo.append(BoloSimples)
            return lista_tipo
        elif tipoBolo == 'T':
            lista_tipo.append(Torta)
            return lista_tipo
        else:
            return 'Digite um tipo existente'
    '''  
      

    #os metodos do contrato

    def buscar(self) -> int: #buscar(IBolo)
        pass

    def cheia(self) -> bool:
        pass
    
    def vazia(self) -> bool:
        pass
    
    def existe(self) -> bool: #existe(IBolo)
        pass

    def consultar(self) -> IBolo: #consultar(IBolo)
        pass

    def listar(self) -> IBolo: #IBolo[]
        pass

    def listar(self) -> str: #IBolo[]
        pass