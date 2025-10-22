numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
numero3 = float(input("Digite outro numero: "))

numeros = [numero1, numero2, numero3]
maior = max(numeros)
menor = min(numeros)

print(f"Maior: {maior}.")
print("Menor: {}.".format (menor))