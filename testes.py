import os
import time

class Estoque:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)
        print("Produto adicionado ao estoque:", produto)

    def remover_produto(self, produto):
        if produto in self.itens:
            self.itens.remove(produto)
            print("Produto removido:", produto)
        else:
            print("Produto não encontrado no estoque.")

    def exibir_estoque(self):
        print("Estoque:")
        for produto in reversed(self.itens):
            print(produto)

    def esta_vazio(self):
        return len(self.itens) == 0

class Pedidos:
    def __init__(self, estoque, vendas):
        self.pedidos = []
        self.estoque = estoque
        self.vendas = vendas

    def registrar_pedido(self, produto):
        self.pedidos.append(produto)

    def processar_pedido(self):
        if not self.estoque.esta_vazio():
            if self.pedidos:
                produto = self.pedidos.pop(0)
                if produto in self.estoque.itens:
                    self.estoque.remover_produto(produto)
                    print("Pedido processado:", produto)
                    print("Obrigado pela compra")
                    self.vendas.registrar_venda(produto, self.estoque)  # Passa o produto e o estoque para vendas
                else:
                    print("Produto não encontrado no estoque.")
            else:
                print("Não há pedidos para processar.")
        else:
            print("Não é possível processar o pedido. Estoque vazio.")

    def exibir_pedidos(self):
        print("Pedidos:")
        for produto in self.pedidos:
            print(produto)



class Vendas:
    def __init__(self):
        self.pilha = []

    def registrar_venda(self, produto, estoque):
        if produto:
            self.pilha.append(produto)
            estoque.remover_produto(produto)  # Remover produto do estoque
            print("Venda registrada:", produto)
        else:
            print("Não é possível fazer a venda. Produto inválido.")

    def desfazer_venda(self, estoque):
        if self.pilha:
            produto = self.pilha.pop()
            estoque.adicionar_produto(produto)  # Adicionar produto de volta ao estoque
            print("Venda desfeita:", produto)
        else:
            print("Não há vendas para desfazer.")

    def exibir_vendas(self):
        print("Vendas:")
        for produto in reversed(self.pilha):
            print(produto)

# Inicializar as estruturas de dados
estoque = Estoque()
vendas = Vendas()
pedidos = Pedidos(estoque, vendas)

while True:
    print("=" * 30)
    print("Opções:")
    print("1. Adicionar produto ao estoque")
    print("2. Remover produto do estoque")
    print("3. Registrar pedido de compra")
    print("4. Processar pedido de compra")
    print("5. Registrar venda")
    print("6. Desfazer última venda")
    print("7. Exibir estoque")
    print("8. Exibir pedidos de compra")
    print("9. Exibir vendas")
    print("10. Sair")
    print("=" * 30)

    try:
        opcao = int(input("Digite sua opção: "))
        time.sleep(1.2)
        if opcao == 1:
            produto = input("Digite o nome do produto: ")
            estoque.adicionar_produto(produto)
            time.sleep(1.2)    
        elif opcao == 2:
            produto = input("Digite o nome do produto que deseja remover: ")
            estoque.remover_produto(produto)
            time.sleep(1.2)
        elif opcao == 3:
            produto = input("Digite o nome do produto: ")
            pedidos.registrar_pedido(produto)
            time.sleep(1.2)
        elif opcao == 4:
            pedidos.processar_pedido()
        elif opcao == 5:
            produto = input("Digite o nome do produto vendido: ")
            vendas.registrar_venda(produto, estoque)
            time.sleep(1.2)
        elif opcao == 6:
            vendas.desfazer_venda(estoque)
        elif opcao == 7:
            estoque.exibir_estoque()
        elif opcao == 8:
            pedidos.exibir_pedidos()
        elif opcao == 9:
            vendas.exibir_vendas()
        elif opcao == 10:
            print("Obrigado por usar nosso sistema! Até logo.")
            time.sleep(1.2)
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
            time.sleep(1.2)
    except ValueError:
        print("Erro: Digite apenas números inteiros para a opção.")
    except Exception as e:
        print(f"Ocorreu um erro:{e}")

    time.sleep(1.2)
    if os.name == 'nt': 
        _ = os.system('cls')
    else:  
        _ = os.system('clear')
