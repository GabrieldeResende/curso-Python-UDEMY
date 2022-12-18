import copy

pessoa = {
    "nome": "Gabriel",
    "sobrenome": "Resende",
    "lista": [0,1,2]
}
print(pessoa)
nome = pessoa.pop("nome")
print(nome)
pessoa.setdefault("idade", 23)
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa["idade"])
pessoa.update({
    "nome": "Robson",
    "moradia": "Brasilia-df",
})
print()
pessoa2 = pessoa.copy() ##deepcopy faz uma copia da lista por inteiro e somente Copy faz uma copia raza!!
pessoa2["nome"] = "Julio"
pessoa2["lista"][1] = 9000
print(pessoa)
print(pessoa2)