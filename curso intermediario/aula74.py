def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

falar_bom_dia = criar_saudacao("bom dia")
falar_boa_noite = criar_saudacao("boa noite")

#print(falar_bom_dia("gabriel"))

for nome in ["gabriel", "joao", "gustavo"]:
    print(falar_boa_noite(nome))
    print(falar_bom_dia(nome))