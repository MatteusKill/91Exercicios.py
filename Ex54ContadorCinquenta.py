print('\n')
print("---------- CONTADOR DE NUMERO 50 ----------")
print("Digite 0 para encerrar.")

contador50 = 0
numero = -1

while numero != 0:
    numero = int(input("Digite um numero: "))
    
    if numero != 0:
        if numero == 50:
            contador50 = contador50 + 1

print('\n')
print("----- RESULTADO -----")
print(f"O numero 50 foi digitado {contador50} vezes.")