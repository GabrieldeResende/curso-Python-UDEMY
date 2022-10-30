"""
iniciar com letra, pode conter numero, separa com ___, letras minusculas
"""
nome = 'gabriel'
idade = 23
altura = 1.70
e_maior = idade > 18
peso = 65
imc = peso / altura ** 2
print("nome: ", nome)
print("idade: ", idade)
print("altura: ", altura)
print("é maior: ", e_maior)

print(nome, "tem", idade, "anos de idade e: seu imc é", imc)  ##formas de declarar as variaveis
print(f'{nome} tem {idade} anos de idade e: seu imc é {imc:.2f}')  ## imc:.2f para casas decimais
print("{} tem {} anos de idade e seu imc é: {}".format(nome, idade, imc))
