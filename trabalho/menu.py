from estoque import estoque

estoques = []

def adicionar_estoque():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    novo_estoque = estoque(nome, preco, quantidade)  # Renomeado aqui
    estoques.append(novo_estoque)
    print("Produto adicionado com sucesso!")

def exibir_estoques():
    if not estoques:
        print("Nenhum produto cadastrado.")
        return
    for estoque in estoques:
        estoque.exibir_informacoes()

def atualizar_preco():
    nome = input("Digite o nome do produto que deseja atualizar o preço: ")
    for estoque in estoques:
        if estoque.nome == nome:
            novo_preco = float(input("Digite o novo preço: "))
            estoque.atualizar_preco(novo_preco)
            return
    print("Produto não encontrado.")

def atualizar_quantidade():
    nome = input("Digite o nome do produto que deseja atualizar a quantidade: ")
    for estoque in estoques:
        if estoque.nome == nome:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque.atualizar_quantidade(nova_quantidade)
            return
    print("Produto não encontrado.")

def atualizar_nome():
    nome = input("Digite o nome do produto que deseja atualizar o nome: ")
    for estoque in estoques:
        if estoque.nome == nome:
            novo_nome = input("Digite o novo nome: ")
            estoque.atualizar_nome(novo_nome)
            return
    print("Produto não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Exibir Produtos")
        print("3. Atualizar Preço")
        print("4. Atualizar Quantidade")
        print("5. Atualizar Nome")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_estoque()
        elif opcao == '2':
            exibir_estoques()
        elif opcao == '3':
            atualizar_preco()
        elif opcao == '4':
            atualizar_quantidade()
        elif opcao == '5':
            atualizar_nome()
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()