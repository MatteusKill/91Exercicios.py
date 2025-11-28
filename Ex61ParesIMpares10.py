print('\n')
print("---------- CONTADOR PAR/IMPAR (10 NUMEROS) ----------")

qntdPares = 0
qntdImpares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i} numero: "))
    
    if numero % 2 == 0:
        qntdPares = qntdPares + 1
    else:
        qntdImpares = qntdImpares + 1

print('\n')
print("----- RESULTADO -----")
print(f"Quantidade de numeros PARES: {qntdPares}")
print(f"Quantidade de numeros IMPARES: {qntdImpares}")