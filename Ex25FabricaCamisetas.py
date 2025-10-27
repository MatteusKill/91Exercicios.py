print('\n')
print('------------------------- SEJA BEM VINDO (A)! -------------------------')
qntdCamisetasPequenas = int(input("Informe a quantidades de camisetas Pequenas selecionadas para a compra: "))
qntdCamisetasMedias = int(input("Informe a quantidades de camisetas Medias selecionadas para a compra: "))
qntdCamisetasGrandes = int(input("Informe a quantidades de camisetas Grandes selecionadas para a compra: "))

precoCamisetasP = 10
precoCamisetasM = 12
precoCamisetasG = 15
valorTotalCamisetas = (precoCamisetasP * qntdCamisetasPequenas) + (precoCamisetasM * qntdCamisetasMedias) + (precoCamisetasG * qntdCamisetasGrandes)

print("\n")
print("----- RESULTADO -----")
print(f"Valor Total da compra: R${valorTotalCamisetas:.2f}.")