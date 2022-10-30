"""
entrada de dados
"""
nome = input("qual seu nome?? ") ##input para entrada de dados pelo usuario
idade = input("qual sua idade?? ")

ano_nascimento = 2022 -int(idade)
print(f"{nome} tem {idade} anos")
print(f"{nome} nasceu em {ano_nascimento}")
