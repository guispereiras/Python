import random 
from br_nome_gen import pessoa_random

print("\n")
print("Um mago das trevas vai atacar um vilarejo e vai invocar 50 esqueletos para atacar com ele.\n")

n1 = int(round(random.randrange(1,50)))
p1 = pessoa_random()


n2 = int(round(random.randrange(1,50)))
p2 = pessoa_random()

h1 = n1, p1
h2 = n2, p2

print("Mas um de maior vitalidade e outro de maior destreza ficarão ao seu lado para o proteger.\n")
print("O esqueleto " f"{p1.nome}" " de número {} e o " f"{p2.nome}" "de número {}" " foram escolhidos para te proteger".format(n1,n2))



