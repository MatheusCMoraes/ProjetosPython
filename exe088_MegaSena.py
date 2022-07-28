from random import randint
from time import sleep
lista_de_jogos = list()

print('=='*15)
print(f'{"JOGA NA MEGA SENA":^30s}')
print('=='*15)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, end=' ')
print(f'SORTEANDO {jogos} JOGOS', end=' ')
print('-='*5)
for Njogos in range(0, jogos):
    lista_de_jogos.append(list())

for jogatina in range(0, jogos): # essa parte cuida de gerar os números e verificar se vão se repitir
    for numeros in range(0, 5):
        lista_de_jogos[jogatina].append(randint(1, 80))
        if numeros > 0: # se não for a primeira interação
            for numeros in lista_de_jogos[jogatina]:  # essa parte usa .count() para remover os repetidos e atribiur um novo valor
                if lista_de_jogos[jogatina].count(numeros) > 1:
                    while lista_de_jogos[jogatina].count(numeros) > 1:
                        lista_de_jogos[jogatina].pop()
                        lista_de_jogos[jogatina].append(randint(1, 80))
                        if lista_de_jogos[jogatina].count(numeros) == 1:
                            break
for ContJogos in range(0, jogos):
    sleep(0.5)
    print(f'Jogo {ContJogos + 1}: {sorted(lista_de_jogos[ContJogos])}')

print('-='*5, end=' ')
print('BOA SORTE', end=' ')
print('-='*5)




