turno = input("Qual turno voce estuda (Ex: M-Matutino, V-Vespertino, N-Noturno): ").upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("Erro! Digite um valor invalido.")