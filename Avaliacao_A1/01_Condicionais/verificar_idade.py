print("Digite 'sair' para encerrar.")

while True:
    entrada = input("Digite a sua idade: ")

    if entrada == "sair":
        break
    
    # Converte o texto para número
    idade = int(entrada)

    if idade >= 18:
        print("Entrada permitida.")
    elif idade >= 16:
        print("Entrada permitida com responsável.")
    else:
        print("Entrada negada.")