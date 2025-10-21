letraDigitada = input("Digite seu sexo abaixo em F-Feminino/M-Masculino: ")

if letraDigitada == "M" or letraDigitada == "m" or letraDigitada == "Masculino" or letraDigitada == "masculino":
    print("Masculino.")
elif letraDigitada == "F" or letraDigitada == "f" or letraDigitada == "Feminino" or letraDigitada == "feminino":
    print("Feminino.")
else:
    print("Valor Invalido!")
