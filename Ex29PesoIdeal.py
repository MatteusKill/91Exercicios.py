print('\n')
print("---------- CALCULADORA DE PESO IDEAL ----------")
alturaPessoa = float(input("Digite a sua altura (em metros): "))
sexoPessoa = input("Digite o seu sexo (M para Masculino, F para Feminino): ")

pesoIdeal = 0

print('\n')
print("----- RESULTADO -----")
if sexoPessoa == "M" or sexoPessoa == "m":
    pesoIdeal = (72.7 * alturaPessoa) - 58
    print(f"Para homens, o peso ideal eh: {pesoIdeal:.2f} kg")
elif sexoPessoa == "F" or sexoPessoa == "f":
    pesoIdeal = (62.1 * alturaPessoa) - 44.7
    print(f"Para mulheres, o peso ideal eh: {pesoIdeal:.2f} kg")
else:
    print("Sexo invalido! Tente novamente.")
