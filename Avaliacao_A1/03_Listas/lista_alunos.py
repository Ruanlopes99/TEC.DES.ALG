# Cria uma lista vazia aonde os dados serao salvos
alunos = []

# mensagem para o usuario
print("Digite os nomes dos alunos. Digite 'sair' para encerrar.")

# um laco de repeticao infinito. caso!!
while True:
    nome = input("Nome do aluno: ")
    
    # comando de parada do while 
    if nome == "sair":
        break 
    
    # Adiciona na lista vazia
    alunos.append(nome)

# Vai mostrar a lista de alunos.
print("\n--- Lista de Alunos ---")
for aluno in alunos:
    print(aluno)