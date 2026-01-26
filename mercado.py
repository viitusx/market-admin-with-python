from typing import List, Dict
from time import sleep

from models.produto import produto
from utils.helper import formata_float_str_moeda


produtor: list[produto] = []
carrinho: list[dict[produto, int]] = []


def main() -> None:
    menu()


def menu(comprar_produto=None) -> None:
    print('==========================')
    print('======Bem-vindo(a)========')
    print('======Mercado Teste=======')
    print('==========================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar produto')
    print('5 - Fechar pedido')
    print('6 - Sair do programa')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produtos()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Saindo do programa')
        sleep(2)
        exit(a)
    else:
        print('Opção Invelida')
        menu()


def cadastrar_produtos() -> None:
    print('Cadastrar produto')
    print('=================')

    nome: str = str(input('Digite o nome do produto: '))
    preco: float = float(input('informe o preço do produto: '))
    
    produto: produto = produto(nome, preco)

    produtos.append(produto)

    print(f'Produto cadastrado com sucesso: {produto}')
    sleep(2)
    menu()

def listar_produto() -> None:
    pass

def visualizar_carrinho() -> None:
    pass

def fechar_pedido() -> None:
    pass

def pega_produto_por_codigo(codigo: int) -> produto:
    pass

if __name__ == '__main__':
    main()
