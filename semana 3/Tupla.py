# Tupla com nomes minúsculos
nomes = ('alice', 'bob', 'lucas')

# Cria uma nova tupla com os nomes convertidos para letras maiúsculas
nomes_maiusculo = tuple(nome.upper() for nome in nomes)

# Exibe a nova tupla
print(nomes_maiusculo)
