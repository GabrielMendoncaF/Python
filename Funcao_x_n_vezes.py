import math
n = float(input("Digite a base: ")) #entrada do número de interações

x_inicial = float(input("Digite o x inicial: ")) #entrada do x inicial

def funcao (x):
    return round((2*(pow(x,3)) + math.cos(x)+10),1) #funcao a ser executada arredondando o resultado para 1 casa decimal

while n > 0:
    print("f (" + str(x_inicial) + ") = " + str(funcao(x_inicial))) #resposta
    n = n -1 #para executar a quantidade de interações necessárias (n vezes)
    x_inicial = x_inicial + 0.5  #adiciona 0.5 ao x inicial
