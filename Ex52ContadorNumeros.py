print('\n')
print("---------- CONTADOR DE ENTRADAS ----------")
print("Digite -1 para encerrar a contagem.")

contador = 0
numero = 0

while numero != -1:
    numero = float(input("Digite um numero: "))
    if numero != -1:
        contador = contador + 1

print('\n')
print("----- RESULTADO -----")
print(f"Foram digitados {contador} numeros.")