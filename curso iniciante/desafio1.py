nome = 'gabriel'
idade = 24
altura = 1.70
peso = 65
ano_Atual = 2022
nascimento = ano_Atual - idade
imc = peso / altura ** 2
print(f"{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso} kg")
print(f"o imc de {nome} é {imc:.2f}")
print(f"{nome} nasceu em {nascimento}")
