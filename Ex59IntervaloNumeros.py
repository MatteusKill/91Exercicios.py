print('\n')
print("---------- GERADOR DE INTERVALO ----------")
numeroA = int(input("Digite o primeiro numero inteiro: "))
numeroB = int(input("Digite o segundo numero inteiro: "))

menor = numeroA
maior = numeroB

if numeroA > numeroB:
    menor = numeroB
    maior = numeroA

print('\n')
print(f"Numeros entre {menor} e {maior}:")

for i in range(menor + 1, maior):
    print(i)