print('\n')
print("---------- CALCULADORA DE FATORIAL ----------")
numeroFatorial = int(input("Digite um numero inteiro para calcular o fatorial: "))

resultado = 1
sequencia = f"{numeroFatorial}! = "

for i in range(numeroFatorial, 0, -1):
    resultado = resultado * i
    if i == 1:
        sequencia = sequencia + f"{i} = "
    else:
        sequencia = sequencia + f"{i}."

print('\n')
print("----- RESULTADO -----")
print(f"{sequencia}{resultado}")