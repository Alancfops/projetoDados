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
    def __init__(self):
        self.pedidos = []

    def registrar_pedido(self, produto):
        self.pedidos.append(produto)

    def processar_pedido(self, estoque):
        if not estoque.esta_vazio():
            if self.pedidos:
                produto = self.pedidos.pop(0)
                if produto in estoque.itens:
                    estoque.remover_produto(produto)
                    print("Pedido processado:", produto)
                    print("Obrigado pela compra")
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
        if not estoque.esta_vazio():
            if produto in estoque.itens:
                self.pilha.append(produto)
                estoque.remover_produto(produto)
                print("Venda registrada:", produto)
            else:
                print("Produto não encontrado no estoque.")
        else:
            print("Não é possível fazer a venda. Estoque vazio.")

    def desfazer_venda(self, estoque):
        if self.pilha:
            produto = self.pilha.pop()
            estoque.adicionar_produto(produto)
            print("Venda desfeita:", produto)
        else:
            print("Não há vendas para desfazer.")

    def exibir_vendas(self):
        print("Vendas:")
        for produto in reversed(self.pilha):
            print(produto)
