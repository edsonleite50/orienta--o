from abc import ABC, abstractmehod

class Movel(ABC):
    @abstractmethod
    def pintar(self) -> None:
        pass


class Cadeira(Movel):
    def pintar(self, numero_de_pes: int) -> None:
        super().__init__()
        self.numero_de_pes = numero_de_pes
        self.cor = None

    def montar(self) -> None:
        pass 


if __name__=='__main__':
    movel = Cadeira(cor='vermelha', numero_de_pes=3)


    print(movel.numero_de_pes)
    print(movel.cor)


    movel.pintar('azul')
    print(movel.cor)