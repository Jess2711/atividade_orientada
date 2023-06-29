from bolo import Bolo
#from iformato import IFormato
from ibolo import IBolo
from bolosimples import BoloSimples
from vetorprateleira import VetorPrateleira
from iprateleira import IPrateleira


bolo1 = BoloSimples(10, False, 'Quadrado') 
bolo1.preco()
print(bolo1)

bolo2= BoloSimples(15, True, 'Circular') 
bolo2.preco()
print(bolo2)

bolo3= BoloSimples(20, False, 'Retangulo') 
bolo3.preco()
print(bolo3)


prateleira = VetorPrateleira(5)
prateleira.inserir(bolo1)
print(prateleira)
prateleira.inserir(bolo2)
print(prateleira)
prateleira.inserir(bolo3)
print(prateleira)
prateleira.inserir(bolo3)
print(prateleira)
prateleira.remover(bolo1)
print(prateleira)
prateleira.remover_posicao(1)
print(prateleira)










'''
segundo_bolo= BoloSimples(10, False, 'Quadrado') 
segundo_bolo.preco()
print(segundo_bolo)
'''



#prateleira.lista_prateleira(IBolo)


#prateleira1.bolo(IBolo)
#print(primeiro_bolo)
#print(isinstance(IPrateleira))
#prateleira2 = VetorPrateleira(1)
#prateleira2.inserir(primeiro_bolo)
#prateleira2.lista_prateleira()
#print(prateleira2)
#primeiro_bolo.inserir()

'''
prateleira3 = VetorPrateleira(1)
prateleira3.inserir(segundo_bolo)
prateleira3.lista_prateleira()
print(prateleira3)
'''
