pessoa = {
    "nome": "Gabriel",
    "sobrenome": "Resende",
    "idade:": 18,
    "altura:": 1.70,
    "endereço: ": [
        {"quadra": 606, "conjunto": 8, "casa": 12},
    ],
}

print(pessoa)
print(pessoa["endereço: "])

for chave in pessoa:
    print(chave, pessoa[chave])