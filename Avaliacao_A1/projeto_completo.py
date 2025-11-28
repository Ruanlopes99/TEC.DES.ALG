# Loop infinito do Menu Principal
while True:
    print("\n=== MENU DE TAREFAS ===")
    print("1 - Verificar Idade")
    print("2 - Contar Pares")
    print("3 - Lista de Alunos")
    print("4 - Cadastro de Produtos")
    print("0 - SAIR")
    
    opcao = input("Escolha uma opção: ")

    # --- OPÇÃO 0: SAIR ---
    if opcao == "0":
        break

    # --- OPÇÃO 1: IDADE ---
    elif opcao == "1":
        print("\n--- Verificação de Idade ---")
        while True:
            entrada = input("Digite a idade (ou 'voltar'): ")
            if entrada == "voltar":
                break
            
            # Conversão e Lógica
            try:
                idade = int(entrada)
                if idade >= 18:
                    print("Entrada permitida.")
                elif idade >= 16:
                    print("Entrada permitida com responsável.")
                else:
                    print("Entrada negada.")
            except:
                print("Digite apenas números.")

    # --- OPÇÃO 2: PARES ---
    elif opcao == "2":
        print("\n--- Pares de 1 a 100 ---")
        print("Usando FOR:")
        for numero in range(1, 101):
            if numero % 2 == 0:
                print(numero)
        
        print("Usando WHILE:")
        contador = 1
        while contador <= 100:
            if contador % 2 == 0:
                print(contador)
            contador = contador + 1

    # --- OPÇÃO 3: ALUNOS ---
    elif opcao == "3":
        print("\n--- Lista de Alunos ---")
        alunos = []
        while True:
            nome = input("Nome do aluno (ou 'sair'): ")
            if nome == "sair":
                break
            alunos.append(nome)
        
        print("Lista final:")
        for aluno in alunos:
            print(aluno)

    # --- OPÇÃO 4: PRODUTOS ---
    elif opcao == "4":
        print("\n--- Cadastro de Produtos ---")
        produtos = {}
        while True:
            nome = input("Nome do produto (ou 'sair'): ")
            if nome == "sair":
                break
            
            preco = float(input("Preço: "))
            produtos[nome] = preco
            
        print("Tabela:")
        for nome, preco in produtos.items():
            print(f"{nome}: R$ {preco}")

    # --- OPÇÃO INVÁLIDA ---
    else:
        print("Opção não existe.")