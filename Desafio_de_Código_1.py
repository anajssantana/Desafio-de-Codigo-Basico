def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

while True:
        consumo_mensal = float(input("Digite o consumo médio mensal de dados em GB: "))
        if consumo_mensal < 0:
                print("O consumo não pode ser negativo. Por favor, insira um valor válido.")
                continue
        elif consumo_mensal >= 0:
            plano_recomendado = recomendar_plano(consumo_mensal)
            print("O plano recomendado é:", plano_recomendado)
            continue

