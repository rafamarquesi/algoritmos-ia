"""
Video aulas do professor Rafael Rossi (https://www.youtube.com/channel/UCRyrXOFjd4VyrjrycLiAKTg)

Primeira parte - Tópicos em Inteligência Artificial - Aula 2 (https://www.youtube.com/playlist?list=PLAHmHkSA6KkVRQoy-bNrax_ZT0AAE1Vhn)
"""

# Funções

def soma(num1, num2):
    resultado = num1 + num2
    return resultado

print(soma(10,15))

def origemDaVida():
    pass

def imprimeDisciplina(nome='Disciplina de SI', semestre=2, ano=2020):
    print('Nome: ', nome)
    print('Semestre: ', semestre)
    print('Ano: ', ano)

imprimeDisciplina('TIA', 2, 2020)

imprimeDisciplina('TIA')

imprimeDisciplina(ano=2030)

def calculaPerimetroArea(largura, altura):
    perimetro = largura * 2 + altura * 2
    area = largura * altura
    return perimetro, area

print(calculaPerimetroArea(5,10))

perimetro, area = calculaPerimetroArea(5,10)

def imprimeParametros(par1, par2, par3):
    print('par1', par1)
    print('par2', par2)
    print('par3', par3)

imprimeParametros('abacate', 'pera', 'maçã')

parametros = ['abacate', 'pera', 'maçã']

imprimeParametros(*parametros)

parametros2 = {
    'par1' : 'abacate',
    'par2' : 'pera',
    'par3' : 'maçã'
}

imprimeParametros(**parametros2)

def soma2(*valores):
    soma = 0
    for num in valores:
        soma += num
    return soma

print(soma2(2,3,4))

soma3 = lambda num1, num2 : num1 + num2
print(soma3(12,32))

def operacao(funcao, num1, num2):
    return funcao(num1, num2)

print(operacao(soma3, 21, 32))

def funcao_modificadora(valor):
    valor = valor + 10
    print(f'Valor dentro da função: {valor}')

variavel = 20
funcao_modificadora(variavel)
print(f'Valor fora da função: {variavel}')

# Orientação a Objetos

class Pessoa():
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def imprime_infos(self):
        print('Nome:', self.nome)
        print('CPF:', self.cpf)
        print('Idade:', self.idade)

    def __eq__(self, other):
        if (self.nome == other.nome) and (self.cpf == other.cpf) and (self.idade == other.idade):
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.idade < other.idade):
            return True
        else:
            return False

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome

class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, curso, rga):
        super().__init__(nome, cpf, idade)
        self.curso = curso
        self.rga = rga

    def imprime_infos(self):
        super().imprime_infos()
        print('Curso:', self.curso)
        print('RGA:', self.rga)

p1 = Pessoa('Rafael', '000.000.000-12', 33)

print(p1.idade)

p1.curso = 'SI'

print(p1.curso)

p1.imprime_infos()

a1 = Aluno('Rafael', '000.000.000-00', 33, 'SI', 00000)
a1.imprime_infos()

p2 = Pessoa('Rafael', '000.000.000-12', 33)
p3 = Pessoa('Rafael', '000.000.000-12', 35)

print(p2 < p3)
print(p2)

class Imperssora(object):

    descricao = 'Essa é uma classe para impressoras'

    def __init__(self, marca, qtd_folhas):
        self.__marca = marca
        self.__qtd_folhas = qtd_folhas

    @property
    def qtd_folhas(self):
        return f'A impressora {self.__marca} possui {self.__qtd_folhas} folhas'

    @qtd_folhas.setter
    def qtd_folhas(self, valor):
        self.__qtd_folhas = valor

    @staticmethod
    def imprime_descricao():
        print(f'Descrição da classe: {Imperssora.descricao}')

    def imprime_infos(self):
        print(f'Marca: {self.__marca}')
        print(f'Qtd de folhas: {self.__qtd_folhas}')

    #
    # def set_qtd_folhas(self, valor):
    #     self.__qtd_folhas = valor
    #
    # def get_qtd_folhas(self):
    #     return self.__qtd_folhas

hp = Imperssora('HP', 100)
print(hp.qtd_folhas)
hp.qtd_folhas = 200
print(hp.qtd_folhas)

print(Imperssora.descricao)
print(Imperssora.imprime_descricao())

lista_objs = [
    Pessoa('rafael','000.000.000-00',33),
    Pessoa('maria','000.000.000-00',34),
    Imperssora('Xerox',100)
]

print(lista_objs)

for obj in lista_objs:
    print('=====')
    obj.imprime_infos()

# String

disciplina = 'Tópicos em Inteligência Artificial'
print(disciplina.capitalize())
print(disciplina.lower())
print(disciplina.upper())
print(disciplina.swapcase())
print(disciplina.startswith('Tópicos'))
print(disciplina.find('Art'))
print(disciplina.split(' '))

tokens = disciplina.split(' ')
print('-'.join(tokens))
print(disciplina.count('Art'))

disciplina2 = '   Sistema de informação    '
print(disciplina2.strip())
print(disciplina2.rstrip())

import re

texto = 'As olimpíadas não ocorrerão mais no ano de 2020. Elas ocorrerão no ano de 2021.'

print(re.findall('[0-9]{4}', texto))

# Arquivos

arquivo = open('batatinha.txt', mode='r')
print(arquivo.read())
arquivo.close()

arquivo = open('batatinha.txt', mode='r')
for linha in arquivo.readlines():
    print(linha.strip())
arquivo.close()

arquivo_in = open('batatinha.txt', mode='r')
arquivo_out = open('batatinha_copia.txt', mode='w')
arquivo_out.write(arquivo_in.read())
arquivo_in.close()
arquivo_out.close()

arquivo_out = open('teste_saida.txt', mode='w')
arquivo_out.write('Teste primeira linha\n')
arquivo_out.close()

arquivo_out = open('teste_saida.txt', mode='a')
arquivo_out.writelines(['Tópicos em IA\n', 'Python\n'])
arquivo_out.close()

lista = ['Tópicos em IA', 'Python', 'Machine Learning', 'Textos', 'Chatbot']
arquivo_out = open('teste_saida.txt', mode='a')
arquivo_out.write('\n'.join(lista))
arquivo_out.close()

with open('batatinha.txt', mode='r') as texto_batatinha:
    print(texto_batatinha.readlines())

arquivo_batatinha = None
try:
    arquivo_batatinha = open('batatinhas.txt', mode='r')
except FileNotFoundError as file_error:
    print('Deu pau!')
    print(file_error.strerror)
finally:
    if arquivo_batatinha != None:
        arquivo_batatinha.close()
    print('Fim do tratamento de exceção')