print('\n')
print("---------- MAIOR E MENOR (20 NUMEROS) ----------")

numero = int(input("Digite o 1 numero: "))
maior = numero
menor = numero

for i in range(2, 21):
    numero = int(input(f"Digite o {i} numero: "))
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

print('\n')
print("----- RESULTADO -----")
print(f"O maior numero digitado foi: {maior}")
print(f"O menor numero digitado foi: {menor}")