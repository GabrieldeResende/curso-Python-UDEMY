# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista3 = lista1 + lista2
# lista4 = list(range(0,100, 8)) #criação de lista com casas multiplas de 8
# print(lista4)
# print(lista2)
# print(max(lista2))  # valor maximo
# print(min(lista2))  # valor minimo
# lista2.pop(0)  # remove o ultimo valor
# del (lista2[0:1])  # deletar valores
# lista2.append("b")  # adicionar valores
# lista2.insert(0, "banana")  # selecionar em qual lugar o valor vai ser adicionado

# print(lista1)
# print(lista2)
# print(lista3)

secreto = "perfume"
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print("voce perdeu!!!")
        break
    letra = input("digite uma letra: ")
    if len(letra) > 1:
        print("digite apenas uma letra!!")
        continue

    digitadas.append(letra)
    print(digitadas)

    if letra in secreto:
        print(f"a letra{letra} existe na palavra")
    else:
        print(f"a letra{letra} nao existe na palavra")
        digitadas.pop()

        print(digitadas)

    secreto_temporario = ''
    for letra_secreta in secreto :
        if letra_secreta in digitadas:
            secreto_temporario = secreto_temporario + letra_secreta
        else:
            secreto_temporario = secreto_temporario + '*'

    if secreto_temporario == secreto:
        print(f"jogo finalizado, a palavra era {secreto_temporario}")
        break
    else:
        print(f"a palavra secreta esta assim: {secreto_temporario}")

    if letra not in secreto:
        chances = chances - 1

    print(f"voce ainda tem {chances} chances")
