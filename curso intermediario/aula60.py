condicao = 10==11
variavel = "valor" if condicao else "outro valor"
print(variavel)

if condicao is True:
    print("valor")
else:
    print("outro valor")

digito = 15
novo_digito = digito if digito <= 9 else 0
novo_digito2 = 0 if digito > 9 else digito
print(novo_digito)
print(novo_digito2)

num1= 2
print("par" if num1 % 2 == 0 else "impar")

if num1 % 2 == 0:
    print("par")
else:
    print("impar")