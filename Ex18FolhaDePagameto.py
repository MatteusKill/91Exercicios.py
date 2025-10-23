print("\n")
print("--------------- FOLHA DE PAGAMENTO PESSOAL---------------")
valorHora = float(input("Quantos voce ganha por hora? "))
horasTrabalhadas = int(input("Quantas horas voce trabalhou este mes? "))

salarioBruto = valorHora * horasTrabalhadas

if salarioBruto <= 900:
    print("Isento de descontos.")
elif salarioBruto <= 1500:
    impostoRenda = 5/100
elif salarioBruto <= 2500:
    impostoRenda = 10/100
else:
    impostoRenda = 20/100

valorIR = salarioBruto * impostoRenda
valorINSS = salarioBruto * (10/100) 
totalDescontos = valorINSS + valorIR
sindicato = - (3/100)
fgts = (11/100)
valorFGTS = salarioBruto * fgts
salarioLiquido = salarioBruto - (valorIR - valorINSS *- sindicato) + fgts

print("\n")
print("---------- RESULTADO ----------")
print(f"Salario bruto: R${salarioBruto:.2f}")
print(f"Desconto aplicado do Imposto de Renda(5%): -R${valorIR:.2f}.")
print(f"Desconto aplicado do INSS(10%): -R${valorINSS:.2f} .")
print(f"Adicionado FGTS(11%): +R${valorFGTS:.2f}.")
print(f"Total de descontos: -R${totalDescontos:.2f} ")
print(f"Salario Liquido: R${salarioLiquido:.2f} ")