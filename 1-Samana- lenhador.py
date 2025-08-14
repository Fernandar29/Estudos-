import random

# Inicialização das variáveis
vida = 10
arvores = 0

# Loop das 3 horas
for hora in range(3):
    print(f"\nHora {hora + 1}: O lenhador cortou uma árvore.")
    print("O goblin apareceu!")
    
    # Entrada do usuário
    acao = input("Você escolheu que o lenhador iria correr ou lutar? ").lower()
    
    # Decisão com base na ação escolhida
    if acao == "correr":
        if random.random() < 0.5:
            print("O lenhador correu, mas não conseguiu levar a árvore!")
        else:
            arvores += 1
            print("O lenhador correu e conseguiu levar a árvore.")
    elif acao == "lutar":
        vida -= 2
        arvores += 1
        print(f"O lenhador lutou e levou 2 de dano. Vida restante: {vida}")
    else:
        vida = 0
        print("Ação inválida! Ele fica parado e o goblin o ataca, tirando toda a vida dele, resultando em morte imediata!!")
        print("O Lenhador morreu!")
        break
    
    # Verificação de vida
    if vida <= 0:
        print("O Lenhador morreu!")
        break

# Cálculo das estacas
estacas = 0
for
