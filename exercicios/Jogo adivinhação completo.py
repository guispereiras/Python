import random
n1 = int(round(random.randrange(1,101)))
rodada = 3
tentativas = 0

print("**********************\n")
print("Jogo da adivinhação\n")
print("**********************\n")

print("Qual nível de dificuldade?")

print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if nivel == 1:
    tentativas = 10
elif nivel == 2:
    tentativas == 5
else: 
    tentativas == 3


for tentativa in range(1, rodada + 1):

    n2 = int(input(("Digite um número entre 1 e 100: ")))

    if (n2 < 1):
        print("Número menor que 1, digite novamente entre 1 e 100.")
    if (n2 > 100):
        print("Número maior que 100, digite novamente entre 1 e 100.")
        continue

    if n2 == n1:
        print("PARABÉNS VOCE ACERTOU LOCAO")
        break
    else:
        if(n2 > n1):
            print("Tente novamente, chute um número mais baixo")
        elif(n2 < n1):
            print("Tente novamente, chute um número mais alto")
    tentativas = tentativas + 1 #serve para conseguir diminuir o while e seguir o loop

print("Fim de jogo\n")
