"""Implemente um sistema de transporte em Python utilizando classes abstratas:

Crie uma classe abstrata Transporte com um atributo capacidade, um método abstrato mover() e um método concreto info() que exibe a capacidade.
Crie duas subclasses:
Carro, que imprime "O carro está se movendo com até X passageiros".
Bicicleta, que imprime "A bicicleta está se movendo com até X pessoas".
No programa principal, crie objetos das duas subclasses, adicione-os em uma lista e invoque mover() e info() para cada um."""

from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, capacidade):
        # if capacidade < 0:
        #     raise ValueError("A capacidade não pode ser negativa")
        self.capacidade = capacidade
    
    @abstractmethod
    def mover(self):
        pass
    
    def info(self):
        print(f"Capacidade: {self.capacidade}")


class Carro(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)
    
    def mover(self):
        return f"O carro está se movendo com até {self.capacidade} passageiros"


class Bicicleta(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)
    
    def mover(self):
        return f"A bicicleta está se movendo com até {self.capacidade} pessoas"


if __name__ == "__main__":
    carro = Carro(2)
    bicicleta = Bicicleta(3)
    
    transportes = [carro, bicicleta]

    for transporte in transportes:
        transporte.info()
        transporte.mover()
