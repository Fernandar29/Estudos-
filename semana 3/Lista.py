# Lista original com números variados
lista = [2, 5, 8, 9, 12, 15, 18]

# Lista que armazenará os números menores ou iguais a 15
nova_lista = []
 
# Adiciona à nova_lista apenas os números <= 15
for numero in lista:
    if numero <= 15:
        nova_lista.append(numero)

# Contador de números pares menores ou iguais a 15
quantidade = 0
for i in lista:
    if i % 2 == 0 and i <= 15:
        quantidade += 1

# Exibe o resultado
print(f"Quantidade de pares: {quantidade} \n\nNova lista {nova_lista}")

