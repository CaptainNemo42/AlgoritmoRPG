import random

#Váriaveis e funções de Personagem(Paladino)
playerLife = int
playerxp = int
playerDmg = int
playerlv = int
playerItens = str
d20 = random.randint(1, 20) #Define se o Jogador vai conseguir ou não fugir, como um D20  

def playerCombat():  #Chamada em todo combate, função para imprimir ações do Jogador
    print("1.Atacar: ", playerDmg, "Dmg. \n")
    print("2.Fugir \n")
    print("3.Abrir Mochila \n")

#Váriaveis e métodos de Inimigos
enemyLife = int
enemytype = ['Orc','Goblin','Thief','Slime']
enemylv = random.randint(1, 10)
enemyspawn=random.choice(enemytype) #Define qual tipo de inimigo irá nascer
enemyDmg = random.randint(1, 15)

#Váriaveis de estrutura
item=['Poção de cura','Espada enferrujada','Totem do desespero','Armadura','Bastão Flamejante']
quest=['Easy''Medium''Hard']
start=bool

def spawnenemy(): #Função de spawn aleatório de inimigo, define se ocorrerá ou não combate
    if d20>=11:
        print("Um ",enemyspawn," Level:", enemylv, "ataca! \n")
        if enemylv>=5:
            enemyLife=6
            enemyDmg=4
            print("O seu inimigo é feroz:", enemyLife,"Life, ",enemyDmg,"Dano")
        elif enemylv<5:
            enemylife=4
            enemyDmg=2
    elif d20 <= 10:
        print("Um Gato de rua passa ao seu lado. \n")

def turno(playerDmg,enemyDmg,playeritens):
    combate=int(input("Escolha uma opção: "))
    if combate == 1:
        if d20>=11:
            playerDmg -= enemyLife
            enemyDmg -=1
        elif d20 <= 10:
            enemyDmg -= playerLife
    elif combate == 2:
        if d20 >=11:
            ("Você escapa com sucesso!")
        if d20 >= 11:
            ("A luta continua, o",enemytype,"Ataca!")
            enemyDmg -= playerLife
    elif combate == 3:
        print(playerItens)
        if playerItens == '0':
            print("Sua mochila está vazia")
        else:
            print("Você possui:", playeritens)
    
#Começo do jogo
print("=====Algoritmo de RPG v1.0====")
day = str(input("Deseja começar o dia? [S/N] \n")) #Váriavel Que inicia o Jogo
if day == 'S':
   start = False 
   playerDmg = 2
   playerLife=8
   playerxp =0
   playerlv=1
elif day == 'N':
    start = True
    print("O jogo encerra aqui...Por enquanto \n")
else:
    print("Try Again, entrada incorreta! \n")
while start == False:
    print("O jogo se inicia, um novo mundo de opções se abre em sua frente, decida seu caminho:" )
    choice = str(input("Escolha o caminho [A/B] para prosseguir \n"))
    if choice == "A":
        print("Uma sábia escolha, sua viagem se inicia de maneira calma, até que...")
        spawnenemy()
        playerCombat()
        turno(playerDmg, enemyDmg,playerItens)
        if enemyLife == 0:
            print("Seu inimigo tomba perante seu poder!")
            playerxp += 25
            drop = random.choice(item)
            print("Você recebe:", playerxp, "e", drop)
        else:
            turno()
        if playerLife == 0:
            start == True
        else:
            turno()
    elif choice == "B":
        print("Um caminho para os ousados, sua viagem é fortuita, até que...")
        spawnenemy()
    else:
        ("Try Again, entrada incorreta!")