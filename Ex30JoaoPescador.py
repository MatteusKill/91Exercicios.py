print("\n")
print("========== MICROSERVICE FISH'ER ==========")
pesoPeixe = float(input("Informe o peso do peixe: "))

c_MultaPorKG = 4
c_KGlimite = 50

if pesoPeixe > 50:
    excessoKG = pesoPeixe - c_KGlimite
    multa = excessoKG * c_MultaPorKG
    print(f'Voce pescou {excessoKG}KG alem do limite.')
    print(f"Devera pagar R${multa}.")
else:
    print("Pescou abaixo do limite estipulado. Nao devera pagar multa.")