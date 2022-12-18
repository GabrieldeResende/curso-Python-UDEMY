lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
print()
print()
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    for produto in produtos
]

print(*novos_produtos, sep="\n")
