#from bolo import Bolo
#from iformato import IFormato
#from ibolo import IBolo
from bolosimples import BoloSimples
from vetorprateleira import VetorPrateleira
#from iprateleira import IPrateleira
from torta import Torta


bolo1 = BoloSimples(10, False, 'Quadrado') 
bolo1.preco()
print(bolo1)

bolo2= BoloSimples(15, True, 'Circular') 
bolo2.preco()
print(bolo2)

bolo3= BoloSimples(20, False, 'Retangulo') 
bolo3.preco()
print(bolo3)

torta1 = Torta(10, '', '', 'Quadrada') 
torta1.preco()
print(torta1)

torta2= Torta(15, '','','') 
torta2.preco()
print(torta2)

torta3= Torta(10, False,'','Circular') 
torta3.preco()
print(torta3)

torta4= Torta(15, '',False,'Circular') 
torta4.preco()
print(torta4)




prateleira = VetorPrateleira(5)
prateleira.listar_tipo_bolo('S')
prateleira.listar_tipo_bolo('T')
#torta1 = (isinstance(torta1, Torta))
print(prateleira)
#print(torta1)

prateleira.inserir(bolo1)
print(prateleira)
prateleira.inserir(bolo2)
print(prateleira)
prateleira.inserir(bolo3)
print(prateleira)
prateleira.inserir(torta1)
print(prateleira)
prateleira.inserir(torta2)
print(prateleira)
prateleira.inserir(torta3)
print(prateleira)
prateleira.inserir(bolo3)
print(prateleira)
prateleira.listar_tipo_bolo('T')
print(prateleira)
prateleira.remover(bolo1)
print(prateleira)
prateleira.remover_posicao(2)
print(prateleira)





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
