from random import *
 
'''
    Gdd jogo copia do show do milhao
 
    Deve ter
    1- Minimo de 15 perguntas
    2- Cada pergunta deve ter 4 perguntas, uma sera correta
    3- A cada pergunta, o jogador deve ter a opçao de escolher
    uma das opções ou parar
    4- Dever ter uma forma de pontuação
    5- Caso escolher parar, a pontuação deverar permanencer a mesma
    5.1- Caso falhe, a pontuação deve decrescer um pouco
    5.2- Pode haver mais estrategias de pontuação
    6- Deverão ter "power ups"
    6.1- Pulo-pula uma questao, somente usado uma vez
    6.2- 50|50- remove metade das questoes erradas, somente 2 usos
    6.3- Plateia- 10 opçoes sorteadas da plateia, cada opçao com 30% de chance
    de estarcorreta, 2 usos
    6.4- Universitarios,5 opções sorteadas, cada opçao com 50% de certeza, 2 usos
    7- Dois manuais
    7.1- Manual de usuario, como jogar o jogo, suas regras e tal
    7.2- Manual de api, oque cada funcao, codigo faz
'''
 
#Global variables
numPoints = 0
numPulos = 0
numCincin = 0
numUni = 0
numPlat = 0
playerName = ''
 
 

 
#Create a random array with n numbers in it
def RandomQuestions(n):
    arr = []
    #Loops and adds i to array
    for i in range(1,n + 1):
        arr.append(i)
    #print(arr)
    return arr
 
#Embaralha as questoes
def ShuffleQuestions():
    newArr = RandomQuestions(15)
    shuffle(newArr)
    #print(newArr)
    return newArr
 
#Make a special question case
#if num is divisible by 5
def SpecialQuestion():
    newArr = ShuffleQuestions()
    oldArr = []
    for i in range(0, len(newArr)):
        if(newArr[i] % 5 == 0 and newArr[i] != 0):
            oldArr.insert(i, newArr[i])
    return oldArr
 
 
 
def Main():
    #O jogo completo estara aki

def pergunta1():
    cachorro=str(input("o cachorro Coragem era? A=Covarde B=Corajoso C=Ciumento ou D=Irritado"))
    if cachorro=='A':
        print("Parabéns, resposta correta.")
    else:
        print("Erroou!!")

def pergunta2():
    carro=str(input("Um carro automático tem quantos pedais? A=4, B=2, C=3 ou D=0"))
    if carro=='B':
        print("Parabéns, resposta correta.")
    else:
        print("Erroou!!")

def pergunta3():
    africa=str(input("A África é um? A=País, B=Cidade, C=continente ou D=Um bairro da cidade de Campo Mourão"))
    if africa=='C':
        print("Parabéns, resposta correta.")
    else:
        print("Erroou!!")

def pergunta4():
    violao=str(input("Um violão comum tem quantas cordas? A=5, B=7, C=8 ou D=6"))
    if violao=='D':
        print("Parabéns, resposta correta.")
    else:
        print("Erroou!!")

def pergunta5():
    exterminador=str(input("A frase marcante do filme 'Exterminador do Futuro' dita pelo proprio Exterminador foi? A=I'll be back, B=I'm back guys, C=What is that? It is a bird? Is it an airplane? No, it's Superman! ou D=God damn"))
    if exterminador=='A':
        print("Parabéns, resposta correta.")
    else:
        print("Erroou!!")


# #List de numeros de questoes no jogo
# questionNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# #Randomicamente embaralha a lista
# shuffle(questionNum)
# print(questionNum)