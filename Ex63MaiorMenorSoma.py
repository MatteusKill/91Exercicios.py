print('\n')
print("---------- RELATORIO DE CONJUNTO DE NUMEROS ----------")
quantidade = int(input("Quantos numeros voce deseja informar? "))

numero = float(input("Digite o 1 numero: "))
maior = numero
menor = numero
soma = numero

for i in range(2, quantidade + 1):
    numero = float(input(f"Digite o {i} numero: "))
    
    soma = soma + numero
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

print('\n')
print("----- RESULTADO -----")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")