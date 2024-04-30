lista_equipamentos = []

print("Digite o nome de até três equipamentos para adicionar à rede:")

    # Loop para solicitar ao usuário inserir até três equipamentos
for i in range(3):
    equipamento = input()
    i += i
    lista_equipamentos.append(equipamento)

print("\nLista de Equipamentos:")
    # Loop para exibir a lista de equipamentos inseridos pelo usuário
for equipamento in lista_equipamentos:
    print(f"- {equipamento}")
