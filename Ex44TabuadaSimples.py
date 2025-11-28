print('\n')
print("---------- GERADOR DE TABUADA ----------")
numeroDigitado = int(input("Digite um numero para ver a tabuada: "))

print('\n')
print(f"----- TABUADA DO {numeroDigitado} -----")

for i in range(1, 11):
    resultado = numeroDigitado * i
    print(f"{numeroDigitado} X {i} = {resultado}")