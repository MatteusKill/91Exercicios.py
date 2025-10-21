nomeUsuario = input("Digite o seu nome: ")
idadeUsuario = int(input("Digite a sua idade: "))

if idadeUsuario <= 2:
    print("Bebê.")
elif idadeUsuario <= 11:
    print("Criança.")
elif idadeUsuario <= 21:
    print("Jovem.")
elif idadeUsuario <= 64:
    print("Adulto.")
elif idadeUsuario <= 100:
    print("Idoso.")
else:
    print("Muito velho.")
