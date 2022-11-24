def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def ola(nome):
    return f"{nome}"
def saudacao(nome, saudacao):
    return f"{nome} {saudacao}"

executando = mestre(ola, "gabriel")
executando2 = mestre(saudacao, "bom dia", "gabriel")
print(executando)
print(executando2)
