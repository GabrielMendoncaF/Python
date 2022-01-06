# variáveis em python

int        = 1                       #int, inteiro
float      = 1.5                     #float, valor decimal
boolean    = True                    #Boolean, True or False
string     = 'palavra'               #String, palavra
list       = [1,1.5,True,'palavra']  #List, uma lista que pode conter diferentes tipos e pode ser alterada
tuple      = (1,1.5,True,'palavra')  #Tuple é como uma lista, porém imutável
tuplaDaTupla = (1,1.5,True,'palavra', tuple) #É possível criar tuplas com tuplas dentro
dictionary = {'chave':'valor',
              'key'  : 'value',
              'dicionário':
                  {'pessoa1':2.5,
                   'pessoa2':20,
                   'pessoa3':True},
              'lista':[1,1.5,False,'palavra']} #armazena itens como "chave:valor" e pode armazenar valores quaisquer
                                               # , ou outras listas ou até mesmo outros dicionários
# o tipo da variável não precisa ser declarado

#Acessando as variáveis
print("variável inteiro :" , int)
print("variável float   :" , float)
print("variável booleana:", boolean)
print("variável string  :" , string)

print("\nACESSANDO A LISTA")
print("lista posição 0 até 3: ", list[0:])
print("lista posição 1: ", list[1])

print("\nMODIFICANDO A LISTA")
print("lista posição 1 = TROCA: ")
list[1] = 'TROCA'
print("lista alterada", list[0:])

print("\nADICIONANDO UM VALOR AO FIM DA LISTA (append)")
list.append('NOVOFIM')
print("lista alterada", list[0:])

print("\nADICIONANDO UM VALOR A QUALQUER LUGAR DA LISTA (insert(position,value))")
list.insert(1,'NOVO VALOR')
print("lista alterada", list[0:])

print("\nREMOVENDO UM VALOR DA LISTA (remove(value))")
list.remove('NOVO VALOR')
print("lista alterada", list[0:])

print("\nREMOVENDO UM VALOR DA LISTA (pop(position))")
list.pop(4)
print("lista alterada", list[0:])





