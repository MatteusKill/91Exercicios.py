print('\n')
print("---------- ESTATISTICA DE ACIDENTES ----------")

maiorIndice = 0
menorIndice = 0
cidadeMaiorIndice = 0
cidadeMenorIndice = 0
somaVeiculos = 0
somaAcidentesMenos2k = 0
contadorCidadesMenos2k = 0

for i in range(1, 6):
    print(f"\nDados da cidade {i}:")
    codigoCidade = int(input("Codigo da cidade: "))
    numeroVeiculos = int(input("Numero de veiculos de passeio: "))
    numeroAcidentes = int(input("Numero de acidentes com vitimas: "))
    
    somaVeiculos = somaVeiculos + numeroVeiculos
    
    if i == 1:
        maiorIndice = numeroAcidentes
        cidadeMaiorIndice = codigoCidade
        menorIndice = numeroAcidentes
        cidadeMenorIndice = codigoCidade
    else:
        if numeroAcidentes > maiorIndice:
            maiorIndice = numeroAcidentes
            cidadeMaiorIndice = codigoCidade
        
        if numeroAcidentes < menorIndice:
            menorIndice = numeroAcidentes
            cidadeMenorIndice = codigoCidade
            
    if numeroVeiculos < 2000:
        somaAcidentesMenos2k = somaAcidentesMenos2k + numeroAcidentes
        contadorCidadesMenos2k = contadorCidadesMenos2k + 1

mediaVeiculos = somaVeiculos / 5

if contadorCidadesMenos2k > 0:
    mediaAcidentes = somaAcidentesMenos2k / contadorCidadesMenos2k
else:
    mediaAcidentes = 0

print('\n')
print("----- RESULTADO -----")
print(f"Maior indice de acidentes: {maiorIndice} (Cidade {cidadeMaiorIndice})")
print(f"Menor indice de acidentes: {menorIndice} (Cidade {cidadeMenorIndice})")
print(f"Media de veiculos nas 5 cidades: {mediaVeiculos}")
print(f"Media de acidentes em cidades com menos de 2000 veiculos: {mediaAcidentes}")