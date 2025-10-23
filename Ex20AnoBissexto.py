print("\n")
print("-------------- VERIFICADOR DE ANO BISSEXTO --------------")
ano = int(input("Digite um ano para verificar se eh bissexto ou nao: "))

print("\n")
print('---------- RESULTADO ----------')
if ano % 100 ==0 and ano % 400==0:
    print(f"{ano} eh bissexto.")
elif ano % 400==0 and not ano%100==0 and ano % 4 ==0:
    print("eh bissexto 2")
else:
    print(f"{ano} nao eh bissexto.")