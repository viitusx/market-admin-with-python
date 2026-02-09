from utils.helper import formata_float_str_moeda


class Produto:
    """Representa um produto com código, nome e valor."""

    _contador: int = 1

    def __init__(self, nome: str, valor: float) -> None:
        self.__codigo: int = Produto._contador
        self.__nome: str = nome
        self.__valor: float = valor

        Produto._contador += 1

    @property
    def codigo(self) -> int:
        """Retorna o código do produto."""
        return self.__codigo

    @property
    def nome(self) -> str:
        """Retorna o nome do produto."""
        return self.__nome

    @property
    def valor(self) -> float:
        """Retorna o valor do produto."""
        return self.__valor

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo}\n"
            f"Nome: {self.nome}\n"
            f"Valor: {formata_float_str_moeda(self.valor)}"
        )
