from models.produto import Produto


def main() -> None:
    produto_x = Produto("Produto X", 3000.0)
    produto_y = Produto("Produto Y", 5000.0)

    print(produto_x)
    print(produto_y)


if __name__ == "__main__":
    main()
