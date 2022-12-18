## split divide uma string
## strip, lstrip, rstrip apaga os espaços
frase = "olha so que coisa interessante"
lista_palavras = frase.split()

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())


print(lista_palavras)

salas = [
    ["primeira lista"],

    ["segunda lista"],

    ["luiz", "eduardo", "helena", (0,10,20,30,40)],
]

print(salas[2][3][4])