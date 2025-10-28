primeiroNumero = int(input("Digite um numero inteiro: "))
segundoNumero = int(input("Digite outro numero inteiro: "))
numeroReal = float(input("Digite um numero real: "))

produto = (primeiroNumero * 2) * (segundoNumero / 2)
soma = (primeiroNumero * 3) + numeroReal
cubo = numeroReal * numeroReal * numeroReal

print('\n')
print(f"O produto do dobro do primeiro com metade do segundo: {produto}.")
print(f"A soma do triplo do primeiro com o terceiro: {soma}.")
print(f"O terceiro elevado ao cubo: {cubo}.")