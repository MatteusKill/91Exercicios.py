print('\n')
print("---------- SOMADOR DE NUMEROS ----------")
print("Digite -999 para encerrar a soma.")

soma = 0
numero = 0

while numero != -999:
    numero = float(input("Digite um numero: "))
    if numero != -999:
        soma = soma + numero

print('\n')
print("----- RESULTADO -----")
print(f"A soma total dos numeros eh: {soma}")