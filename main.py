from bolo import Bolo
from formato import IFormato
from ibolo import IBolo
from bolosimples import BoloSimples

primeiro_bolo= BoloSimples('quadrado', 20, True) #é passado ou vem do formato do bolo?
primeiro_bolo.preco()
print(primeiro_bolo)