print('\n')
print("---------- CADASTRO ----------")
nomePessoa = input("Digite o nome: ")
sexoPessoa = input("Digite o sexo (M/F): ")
estadoCivil = input("Digite o estado civil (SOLTEIRA/CASADA): ")

if (sexoPessoa == "F" or sexoPessoa == "f") and (estadoCivil == "CASADA" or estadoCivil == "casada"):
    tempoCasada = int(input("Quantos anos de casada? "))
    print('\n')
    print("----- DADOS -----")
    print(f"Nome: {nomePessoa}")
    print(f"Tempo de casamento: {tempoCasada} anos")
else:
    print('\n')
    print("----- DADOS -----")
    print(f"Nome: {nomePessoa}")
    print(f"Estado Civil: {estadoCivil}")