from utils.helper import formata_float_str_moeda

    class produto:
        contador: int = 1

        def __init__(self, nome: str, valor: float) -> None:
            self.__codigo: int = produto.contador
            self.__nome: str = nome
            self.__valor: float = valor
            produto.contador +=1

        @property
        def nome(self: object) -> int:
            return self.__codigo

        @property
        def valor(self: object) -> str:
            return self.__nome

        @property
        def valor(self: object)  -> float:
            return self.__valor

        def __str__(self: object) -> str:
            return f'codigo: {self.codigo} \nnome: {self.nome} \nvalor: {formata_float_str_moeda(self.valor)}'





