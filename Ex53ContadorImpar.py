print('\n')
print("---------- CONTADOR DE IMPARES ----------")
print("Digite -999 para encerrar.")

contadorImpares = 0
numero = 0

while numero != -999:
    numero = int(input("Digite um numero: "))
    
    if numero != -999:
        if numero % 2 != 0:
            contadorImpares = contadorImpares + 1

print('\n')
print("----- RESULTADO -----")
print(f"Quantidade de numeros impares digitados: {contadorImpares}")