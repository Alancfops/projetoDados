from classe import *
import time
import os

estoque = Estoque()
vendas = Vendas()
pedidos = Pedidos(estoque, vendas)#novo, chama a venda como parametro

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
