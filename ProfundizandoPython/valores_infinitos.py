#manejo de valores infinitos
import math
from decimal import Decimal

infinito_positivo = float('inf')
print(f'a={infinito_positivo}')
infinito_negativo=float('-inf')
print(f'a={infinito_negativo}')


infinito_positivo=math.inf
print(f'a={infinito_positivo}')
print(f'Es infinito?{math.isinf(infinito_positivo)}')

infinito_negativo=-math.inf
print(f'a={infinito_negativo}')
print(f'Es infinito?{math.isinf(infinito_negativo)}')

#decimal

infinito_positivo=Decimal('Infinity')
print(f'a={infinito_positivo}')
print(f'Es infinito?{math.isinf(infinito_positivo)}')

infinito_negativo=Decimal('-Infinity')
print(f'a={infinito_negativo}')
print(f'Es infinito?{math.isinf(infinito_negativo)}')
