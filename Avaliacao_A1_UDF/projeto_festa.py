print(">>> SISTEMA INICIADO")

# Loop Infinito: O programa roda para sempre até alguém escolher '0'

while True:
    # Mostra o Menu de Opções
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Portaria (Verificar Idade)")
    print("2 - Sorteio de Rifas (Pares)")  
    print("3 - Lista VIP (Nomes)")    
    print("4 - Consumação (Aniversariantes)")
    print("0 - SAIR")
    
    # Recebe a escolha do usuário
    opcao = input("Escolha uma opção: ")


    # OPÇÃO 0: SAIR
    if opcao == "0":
        print("Fechando o sistema...")
        break # O 'break' quebra o loop while e encerra o programa

    
    # OPÇÃO 1: PORTARIA (Uso de IF / ELIF / ELSE)
    elif opcao == "1":
        print("\n--- PORTARIA (Checagem de Idade) ---")
        
        while True:
            # Pede a idade ou o comando de saída
            entrada = input("Digite a idade (ou 'voltar'): ")
            
            # Se digitar 'voltar', sai desse loop e volta pro menu
            if entrada == "voltar":
                break
            
            # Try/Except: Protege contra erros se digitar letras
            try:
                idade = int(entrada) # Converte texto para número
                
                # Regras de Entrada
                if idade >= 18:
                    print(">> Entrada Liberada (Pulseira Dourada).")
                elif idade >= 16:
                    print(">> Entrada Liberada (Pulseira Prata - Responsável).")
                else:
                    print(">> Entrada Negada (Menor de 16).")
                    
            except ValueError:
                print("ERRO: Digite apenas números.")

    
    # OPÇÃO 2: RIFAS (Uso de FOR e WHILE)
    elif opcao == "2":
        print("\n--- GERADOR DE RIFAS (Apenas Pares) ---")
        
        print("Usando FOR:")
        # O range(1, 101) gera números de 1 a 100
        for numero in range(1, 101):
            # O símbolo % verifica o resto da divisão. Se for 0, é PAR.
            if numero % 2 == 0:
                print(numero, end=" ") # end=" " imprime na mesma linha
        
        print("\n\nUsando WHILE:")
        contador = 1
        while contador <= 100:
            if contador % 2 == 0:
                print(contador, end=" ")
            contador = contador + 1
        
        print("\n") # Pula linha no final

    
    # OPÇÃO 3: LISTA VIP (Uso de LISTAS [])
    elif opcao == "3":
        print("\n--- LISTA DE CONVIDADOS VIP ---")
        convidados = [] # Cria uma lista vazia
        
        while True:
            nome = input("Nome do convidado (ou 'sair'): ")
            
            if nome == "sair":
                break
            
            # .append() adiciona o nome no final da lista
            convidados.append(nome)
            print("Nome adicionado.")
            
        print("\n--- RESUMO DA LISTA ---")
        # Lê a lista item por item
        for pessoa in convidados:
            print(f"VIP: {pessoa}")

   
    # OPÇÃO 4: ANIVERSARIANTES (Uso de DICIONÁRIOS {})
    elif opcao == "4":
        print("\n--- CONTROLE DE CONSUMAÇÃO ---")
        aniversariantes = {} # Cria um dicionário vazio
        
        while True:
            nome = input("Nome do Aniversariante (ou 'sair'): ")
            
            if nome == "sair":
                break
            
            try:
                valor = float(input(f"Valor liberado para {nome}: R$ "))
                
                # Guarda no dicionário: CHAVE (Nome) = VALOR (Dinheiro)
                aniversariantes[nome] = valor
                print("Consumação registrada.")
                
            except ValueError:
                print("ERRO: O valor deve ser numérico.")
                
        print("\n--- TABELA DE BENEFÍCIOS ---")
        # .items() pega o par (Nome e Valor) para mostrar
        for nome, valor in aniversariantes.items():
            print(f"{nome}: R$ {valor:.2f}")


    # OPÇÃO INVÁLIDA
    else:
        print("Opção não existe. Tente 1, 2, 3, 4 ou 0.")