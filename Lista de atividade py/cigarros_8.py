idade = int(input("\nDigite sua idade: "))
cigarros_por_dia = int(input("\nDigite quantos cigarros você fuma por dia: "))

total_cigarros = cigarros_por_dia * (365 * idade)

minutos_perdidos = total_cigarros * 10

dias_perdidos = minutos_perdidos / (24 * 60)

print(f"\nVocê perdeu aproximadamente {dias_perdidos:.2f} dias de vida devido ao hábito de fumar.")