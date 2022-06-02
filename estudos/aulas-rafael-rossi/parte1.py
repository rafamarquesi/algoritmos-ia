"""
Video aulas do professor Rafael Rossi (https://www.youtube.com/channel/UCRyrXOFjd4VyrjrycLiAKTg)

Primeira parte - Tópicos em Inteligência Artificial - Aula 1 (https://www.youtube.com/playlist?list=PLAHmHkSA6KkW8RzHhnzu5SIUqI4a8ogRH)
"""

# Tipos básicos

## Inteiros

var_int = 10

print(type(var_int))

## Flutuante

var_flutuante = 10.5

print(type(var_flutuante))

print(var_flutuante + var_int)

## Complexo

var_complexo = 0.2j

print(type(var_complexo))

## Boolean

var_bool = False

print(type(var_bool))

## String

var_str1 = 'String em Python'
print(var_str1)

var_str2 = 'String em Python2'
print(var_str2)

var_str1 + str(var_int)

print('=' * 10)

## Listas

lista1 = [1,'Abacate',58.4,30]
print(type(lista1))

print(lista1)

lista2 = [1,3,4] + [32,65,76]
print(lista2)

lista2 = lista2 + [4]

lista2.append(6)

print(lista2)

lista2.insert(2,9)

print(lista2)

print(lista2.index(9))

lista2.sort()
print(lista2)

lista2.reverse()
print(lista2)

lista2.remove(9)
print(lista2)

print(lista2[2])

print(lista2)

del lista2[2]
print(lista2)

lista3 = [
    [10,20,30],
    [40,50,60]
]
print(lista3[0][1])

print(lista2[1:4])
print(lista2[1:])

print(var_str2)
print(var_str2[1:])

print(lista2[:4])
print(lista2[:-1])
print(var_str2[:-1])
print(len(var_str2))

lista4 = lista2.copy()

lista4[2:5] = [0,0,0]
print(lista4)

lista2 = lista2 + [23,43,64,123,543,52]
print(lista2)
print(lista2[1:10:2])

## Tupla

var_tupla = ('Rafael', 33, '000.000.000-00')
print(type(var_tupla))
print(var_tupla)
print(var_tupla[0])

lista_alunos = [
    ('Rafael', '342'),
    ('João', '235'),
    ('Maria', '0934')
]
print(lista_alunos)
print(lista_alunos[0][0])

## Dicionario

var_dict = {
    'POO' : 'Programação Orientada a Objetos',
    'TIA' : 'Tópicos em Inteligência Artificial'
}
print(type(var_dict))

print(var_dict['TIA'])

var_dict1 = {
    1 : 'POO',
    'ABC' : 20
}
print(var_dict1[1])

print('POO' in var_dict)

var_dict['SOI'] = 'Sistemas Operacionais I'
print(var_dict)

var_dict.update({'SOII' : 'Sistemas Operacionais II'})
print(var_dict)

del var_dict['SOI']
print(var_dict)

## Conjuntos

var_set = {1,1,2,2,2,3,3,3,4,4,4,5}
print(type(var_set))
var_set.add(20)
print(var_set)

var_set2 = {4,5,30,40}
print(var_set2)

var_set3 = var_set.union(var_set2)
print(var_set3)

print(var_set.intersection(var_set2))
print(var_set.difference(var_set2))
var_set.remove(1)
print(var_set)

# Operadores Matemáticos
## Soma
print(10+20)
## Subtração
print(50-25)
## Divisão
print(10/8)
## Multiplicação
print(5*4)
## Resto da Divisão
print(10%4)
## Parte inteira da divisão
print(10 // 4)
## Elevação
print(16**0.5)
## Atribuição Composta
a = 10
a += 20
print(a)

# Entrada e Saída
##Entrada

# nome = input('Digite o seu nome: ')
nome = 'rafael'
print(nome)

# idade = input('Digite sua idade: ')
idade = '33'
print(idade)
idade = int(idade)
print(type(idade))

# altura = input('Digite a sua altura: ')
altura = 1.8
print(altura)

print('O nome é '+ nome + ', e a idade é ' + str(idade))
print('O nome é', nome, 'e a idade é', idade)

print('O nome é %s, e a idade é %d' % (nome, idade))
print('O nome é {}, e a idade é {}'.format(nome, idade))
print(f'O nome é {nome}, e a idade é {idade}')
print(f'O nome é {nome}, e a idade é {idade}, e a altura é {altura:.3f}')

tabuada = 2
for num in range(1,11):
    print(f'{tabuada} x {num:2} = {tabuada * num:3}')

print(r'\n')

# Controle de Fluxo
## Testes Lógicos

print(10 == 10)
print('abacate' == 'abacate')
print(10 != 20)
print(10>20)
print(30 >= 10)
print(30 > 20 and 'abacate' == 'abacate')
print(30 > 20 or 'abacate' == 'abacaxi')
print((30 > 20) ^ ('abacate' == 'abacate'))
print(not (30>20))

print(lista1 == lista2)

## Estrutura de Seleção
nota = 5
if nota >= 6 : print('Aprovado')

nota = 8
if nota >= 6 :
    print('Aprovado')
else:
    print('Reprovado')

nota = 4
if nota < 3 :
    print('Reprovado')
elif nota < 6:
    print('Recuperação')
elif nota <=10:
    print('Aprovado')
else:
    print('Nota Inválida')

## Estruturas de Repetição

lista_cidades = ['Porto Ferreira', 'Três Lagoas', 'Andradina', 'Ilha Solteira']

contador = 1
tabuada = 5
while contador <= 10:
    print(f'{tabuada} * {contador:<2} = {tabuada * contador}')
    contador += 1

contador = 0
while contador < len(lista_cidades):
    print(lista_cidades[contador])
    contador += 1

for cidade in lista_cidades:
    print(cidade)

for indice in range(len(lista_cidades)):
    print(indice, '-', lista_cidades[indice])

for indice, valor in enumerate(lista_cidades):
    print(indice, '-', valor)

for chave, valor in var_dict.items():
    print(chave, '-', valor)

list_comp1 = [num for num in range(1,11)]
print(list_comp1)

list_comp2 = [num * 2 for num in range(0,6)]
print(list_comp2)

list_comp3 = [num for num in range(0,51) if num % 3 ==1]
print(list_comp3)

print(lista_cidades)

nova_lista_cidades = [cidade.lower() for cidade in lista_cidades]
print(nova_lista_cidades)

# None

operacao = None
if (operacao == 1):
    print('op igual a 1')
else:
    print('op diferente de 1')

print(type(operacao))
