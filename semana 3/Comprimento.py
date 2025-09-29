import math

ld = 8  # Define o comprimento do lado do hexágono
r3 = 1.732  # Aproximação da raiz quadrada de 3

# Fórmula para calcular a área de um hexágono regular: (3√3/2) * lado²
resultado = (3*r3/2) * (ld**2)

# Arredonda o resultado para 2 casas decimais
arredondamento = round(resultado, 2)

# Exibe o resultado formatado
print('A área do hexágono é de :', arredondamento, 'centimetros ao quadrado.')

