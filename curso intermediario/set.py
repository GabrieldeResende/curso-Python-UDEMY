# s1 = set()  # set vazio
s1 = {"gabriel", 1, 2, 3}  # set com dados
s1.add("Resende")  # para adcionar itens
print("gabriel" in s1)
s1.update(("ola mundo",))  # para adcionar itens sem bagunçar a ordem
# s1.clear() #para limpar o set
print(s1)
s1.discard("Resende")  ##para eliminar algum item do set, colocar um item em cada discard
print(s1)
print()
print()

s2 = {4, 5, 6}
s3 = {6, 5, 8}
s4 = s2 | s3  # para uniao
s5 = s2 & s3  # itens presente nos dois sets
s6 = s2 - s3  # itens que estao somente no set da esquerda
s7 = s2 ^ s3  # itens que nao estao presente nos dois sets
print(s4)
print(s5)
print(s6)
print(s7)
print()
print()

lista = [ 4, 2, 1, 6, 1, 4, 4 ]

qtd = len( set( [ item for item in lista if lista.count( item ) > 1] ) )

print( qtd )
