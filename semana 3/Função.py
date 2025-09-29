# Função que soma os elementos de uma lista
def soma_lista(lista):
    total = 0
    for num in lista:
        total += num  # Acumula cada valor na variável 'total'
    return total  # Retorna a soma total

# Chamada da função com a lista [1, 2]
lista = [1, 2]
print(soma_lista(lista))  # Saída será 3

