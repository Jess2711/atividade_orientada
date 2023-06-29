from abc import ABC, abstractmethod

class IBolo(ABC): #só tem 1 metodo fazer o calculo 
#implementar o calculo de venda do bolo custo*área do bolo(quadrado, retangular, circular etc)
#Ela define o método preco() responsável por calcular o preço de venda do bolo a depender de suas características.
    @abstractmethod
    def preco(self) -> float:
        pass #implementar o calculo de venda do bolo custo*área do bolo(quadrado, retangular, circular etc)
    #Ela define o método preco() responsável por calcular o preço de venda do bolo a depender de suas características.