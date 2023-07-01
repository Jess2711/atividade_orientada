
from iprateleira import IPrateleira
from ibolo import IBolo
from bolosimples import BoloSimples
from torta import Torta

#classe concreta que implementa a interface IPrateleira
class VetorPrateleira():
    def __init__(self, tamanho: int):
        self._prateleira_bolos:IBolo = [] #esse atributo do tipo lista precisa ser encapsulado?
        self._tamanho = tamanho
        IPrateleira.register(VetorPrateleira)

    #metodos acessadores e modificadores:
    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, valor):
        self._tamanho = valor
    
    #isso aqui eu criei para testar isinstance, não está sendo usado mas vou deixar aqui como exemplo
    def existe(self, obj) -> bool: 
        if (isinstance(obj, IPrateleira)):
            obj.inserir()
            return True
        else:
            print('Não tem bolo')
            return False

    #essa função trouxe da classe bolo para tentar fazer funcionar na função inserir, não funcionou.
    '''
    def equals(self, obj):  
        if (isinstance(obj, Bolo)):
           return self.codigo == obj.codigo
        return False 
    '''   
    #implemtando os métodos do contrato:
    #O método deverá lançar uma mensagem “Bolo já cadastrado.” caso exista na prateleira pelo menos um bolo com 
    #o mesmo código, método da interface.    
    def inserir(self, bolo: IBolo) -> bool:  
        #percorrer a lista de bolos dentro de for (não deu certo com a função equals, se já existe não insere)
        for obj_bolo in self._prateleira_bolos:  
            if obj_bolo.codigo == bolo.codigo:
                print('Bolo já cadastrado')
                return
        if len(self._prateleira_bolos) < self.tamanho:
            self._prateleira_bolos.append(bolo)
            print('Bolo inserido')
        else:
            print('Prateleira cheia')
        print(self._prateleira_bolos)

    #remove um bolo específico da prateleira   
    def remover(self, bolo) -> IBolo: #IBolo bolo
        if bolo in self._prateleira_bolos:
            self._prateleira_bolos.remove(bolo)
            print('Bolo:', bolo, 'Removido com sucesso')
        else: 
            print('Bolo inexistente')

    #remove um bolo na posição especificada
    def remover_posicao(self, posicao) -> int: #IBolo bolo
        if posicao<len(self._prateleira_bolos) and self._prateleira_bolos[posicao] in self._prateleira_bolos:
            del self._prateleira_bolos[posicao]
            print('Bolo removido da posição:', posicao)
        else: 
            print('Bolo inexistente')
    '''
    o método listar_tipo_bolo(char tipoDoBolo) é responsável por retornar uma lista de
    bolos do tipo especificado. Caso o tipoDoBolo seja “S”, a lista deverá conter apenas
    exemplares de bolos do tipo BoloSimples. Caso o tipoDoBolo seja “T”, a lista deverá
    conter apenas exemplares de bolos do tipo Torta.
    '''
    def listar_tipo_bolo(self, tipo:str):
        lista_tipo = []
        if tipo == 'S':
            for bolo in self._prateleira_bolos:  
                if (isinstance(bolo, BoloSimples)):
                    lista_tipo.append(bolo)
                    print(lista_tipo)
        elif tipo == 'T':
            for bolo in self._prateleira_bolos:  
                if (isinstance(bolo, Torta)):
                    lista_tipo.append(bolo)
                    print(lista_tipo)
        else:
            print('Digite um tipo existente')
        #return lista_tipo usando o return não imprime nada 
      
    #os outros metodos do contrato para o restante da equipe implementar

    def buscar(self) -> int: #buscar(IBolo)
        pass

    def cheia(self) -> bool:
        pass
    
    def vazia(self) -> bool:
        pass
    
    def consultar(self) -> IBolo: #consultar(IBolo)
        pass

    def listar(self) -> str: #IBolo[]
        pass