"""
operadores logicos
and, or, not
in e not in
"""
##comparacao1 and comparacao2
##comparacao1 e comparacao2

##comparacao1 or comparacao2
##comparacao1 ou comparacao2

##comparacao1 in comparacao2
##comparacao1 esta comparacao2
##ex:: se tiver A em Gabriel retorna verdadeiro, senao falso

##comparacao1 notin ##comparacao2
##comparacao1 naoesta ##comparacao2

usuario = input("digite seu nome: ")
senha = input("digite sua senha: ")

usuario_bd = 'gabriel'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print("voce esta logado no sistema")
else:
    print("usuario ou senha invalidos!!!")
