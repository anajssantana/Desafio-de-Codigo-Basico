import re

def validar_numero_telefone(numero):
    # Definir o padrão de regex para validar o número de telefone
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"

    # Verificar se o número de telefone corresponde ao padrão
    if re.match(padrao, numero):
        return "Número de telefone válido!"
    else:
        return "Número de telefone inválido. O formato esperado é: (XX) 9XXXX-XXXX"

# Exemplo de uso da função
numero_telefone = input("Digite o número de telefone: ")
resultado = validar_numero_telefone(numero_telefone)
print(resultado)
