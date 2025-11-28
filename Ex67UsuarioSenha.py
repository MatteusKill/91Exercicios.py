print('\n')
print("---------- CADASTRO DE USUARIO ----------")

while True:
    nomeUsuario = input("Digite o nome de usuario: ")
    senhaUsuario = input("Digite a senha: ")
    
    if nomeUsuario != senhaUsuario:
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro: A senha nao pode ser igual ao nome de usuario. Tente novamente.\n")