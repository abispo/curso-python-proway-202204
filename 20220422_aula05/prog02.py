"""
CoffeeMachine

A máquina de café terá que armazenar café, água, açúcar e leite e
chocolate
O usuário poderá escolher a bebida que quiser por meio de botões.
As opções serão:
    - Café (Café + água)
    - Cappuccino (Café + chocolate + água)
    - Leite (Leite + água)

Os ingredientes serão armazenados e misturados quando o usuário
escolher uma das opções.

"""

from time import sleep
from random import randint

class CoffeeMachine:

    def __init__(self, coffee=1000, milk=500, chocolate=500, water=1000):
        # Quando queremos indicar que um atributo ou método deve ser
        # tratado como privado, iniciamos o nome desse atributo ou
        # método com underline '_'
        self._coffee = coffee
        self._milk = milk
        self._chocolate = chocolate
        self._water = water

        print("Máquina de café ligada...")

    # As properties em Python funcionam de forma semelhante aos
    # métodos getters e setters do Java. Vamos acessar os atributos
    # privados a partir de um atributo público
    @property
    def coffee(self):
        return self._coffee

    def _make_coffee(self):
        if self._coffee >= 5 and self._water >= 50:
            print("Preparando o café...")
            sleep(randint(1, 5))

            # self._coffee = self._coffee - 5
            self._coffee -= 5
            self._water -= 50


    def _make_cappuccino(self):
        pass

    def _make_milk(self):
        pass

    def make_drink(self, option):
        if option == 1:
            self._make_coffee()
        elif option == 2:
            pass
        elif option == 3:
            pass


if __name__ == '__main__':
    coffee_machine = CoffeeMachine()
    print(coffee_machine.coffee)

    output = f"""
    Escolha a sua opção:
    
    1 - Café
    2 - Cappuccino
    3 - Leite
    """

    print(output)

    option = int(input("Opção: "))
    coffee_machine.make_drink(option)
