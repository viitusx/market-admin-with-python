from time import sleep
from typing import List, Dict

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print("==========================")
    print("====== Bem-vindo(a) ======")
    print("====== Mercado Teste =====")
    print("==========================")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Visualizar carrinho")
    print("5 - Fechar pedido")
    print("6 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido.")
        sleep(1)
        return menu()

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Saindo do programa...")
        sleep(1)
        exit()
    else:
        print("Opção inválida.")
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print("Cadastrar produto")
    print("=================")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))

    produto = Produto(nome, preco)
    produtos.append(produto)

    print(f"Produto cadastrado com sucesso:\n{produto}")
    sleep(2)
    menu()


def listar_produtos() -> None:
    if produtos:
        print("Produtos cadastrados")
        print("--------------------")
        for produto in produtos:
            print(produto)
            print("--------------------")
            sleep(1)
    else:
        print("Ainda não existem produtos cadastrados.")

    sleep(2)
    menu()


def comprar_produto() -> None:
    if not produtos:
        print("Ainda não existem produtos cadastrados.")
        sleep(2)
        return menu()

    print("Produtos disponíveis")
    print("--------------------")
    for produto in produtos:
        print(produto)
        print("--------------------")
        sleep(1)

    codigo = int(input("Informe o código do produto: "))
    produto = pega_produto_por_codigo(codigo)

    if not produto:
        print("Produto não encontrado.")
        sleep(2)
        return menu()

    for item in carrinho:
        if produto in item:
            item[produto] += 1
            print(f"{produto.nome} agora tem {item[produto]} unidade(s) no carrinho.")
            sleep(2)
            return menu()

    carrinho.append({produto: 1})
    print(f"{produto.nome} foi adicionado ao carrinho.")
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if not carrinho:
        print("Carrinho vazio.")
        sleep(2)
        return menu()

    print("Produtos no carrinho")
    print("--------------------")

    for item in carrinho:
        for produto, quantidade in item.items():
            print(produto)
            print(f"Quantidade: {quantidade}")
            print("--------------------")
            sleep(1)

    sleep(2)
    menu()


def fechar_pedido() -> None:
    if not carrinho:
        print("Carrinho vazio.")
        sleep(2)
        return menu()

    valor_total = 0.0
    print("Resumo do pedido")
    print("----------------")

    for item in carrinho:
        for produto, quantidade in item.items():
            print(produto)
            print(f"Quantidade: {quantidade}")
            valor_total += produto.valor * quantidade
            print("----------------")
            sleep(1)

    print(f"Total a pagar: {formata_float_str_moeda(valor_total)}")
    print("Volte sempre!")
    carrinho.clear()
    sleep(3)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto | None:
    for produto in produtos:
        if produto.codigo == codigo:
            return produto
    return None


if __name__ == "__main__":
    main()
z