print('\n')
print("---------- CRESCIMENTO POPULACIONAL ----------")

populacaoA = 80000
taxaA = 0.03
populacaoB = 200000
taxaB = 0.015
anos = 0

while populacaoA < populacaoB:
    populacaoA = populacaoA + (populacaoA * taxaA)
    populacaoB = populacaoB + (populacaoB * taxaB)
    anos = anos + 1

print('\n')
print("----- RESULTADO -----")
print(f"Populacao Pais A: {int(populacaoA)} habitantes")
print(f"Populacao Pais B: {int(populacaoB)} habitantes")
print(f"Anos necessarios para A ultrapassar ou igualar B: {anos} anos")