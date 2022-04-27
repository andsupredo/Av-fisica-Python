print('Avaliação de composição corporal')
print('================================')

from classes import *

a1 = MassaMuscular()

print(a1.imc())
print(a1.calculo_gordura())
print(a1.calculo_musc())
