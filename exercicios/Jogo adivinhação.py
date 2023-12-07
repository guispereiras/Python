print("**********************\n")
print("Jogo da adivinhação\n")
print("**********************\n")
tentativas = 1
numerochute = 42
rodada = 3

for tentativa in range(1, rodada + 1):
    n1 = int(input("Digite seu número, ele deve ser entre 1 e 100: "))
    if (n1 < 1 or n1 >100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    
    print("Rodada", tentativas, "de", rodada)
    
    if n1 == numerochute:
        print("Voce acertou!")
        break
    else:
        if (n1 < numerochute):
            print("Tente chutar mais alto")
        elif (n1 > numerochute):
            print("tente chutar mais baixo")
    
    tentativas = tentativas + 1 #serve para conseguir diminuir o while e seguir o loop

print("Fim de jogo\n")