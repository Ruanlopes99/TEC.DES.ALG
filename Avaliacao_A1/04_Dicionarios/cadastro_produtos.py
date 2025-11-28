# Cria um dicionário vazio aonde sera salvos os prdutos com seu preco
produtos = {}

# Menssagem ao usuario informando
print("Cadastro de Produtos. Digite 'sair' no nome para encerrar.")


3
while True:
    nome = input("Nome do produto: ")
    if nome.lower() == "sair":
        break
    
    preco = float(input("Preço do produto: R$ "))
    
    # Salva no dicionário: Chave (nome) = Valor (preço)
    produtos[nome] = preco

print("\n--- Produtos Cadastrados ---")
# Mostra item por item
for nome, preco in produtos.items():
    print(f"Produto: {nome} | Preço: R$ {preco:.2f}")
