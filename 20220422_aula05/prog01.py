
# Usamos 'class' para criar uma classe
class Pokemon:

    # __init__ é o método inicializador da classe
    # Alguns chamam também de método construtor
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    # self é uma referência da própria classe que foi instanciada
    def attack(self):
        print("O Pikachu atacou!")

    def dodge(self):
        print("O Pikachu se esquivou!")

    def evolve(self):
        self.name = "Raichu"
        self.health = 120
        print("Pikachu evoluiu para Raichu!")

    def info(self):
        # Quando usamos f-strings, sempre precisamos colocar o f antes
        # da string
        output = f"""
            Nome: {pikachu.name}
            Tipo: {pikachu.type}
            HP: {pikachu.health}
            """

        print(output)

# 0x000001D10CA4F8B0
if __name__ == '__main__':

    # Da maneira abaixo instanciamos a classe Pokemon, criando o
    # objeto pikachu

    # Quando instanciamos uma classe, o método __init__ é chamado
    pikachu = Pokemon("Pikachu", "Elétrico", 70)

    # Podemos alterar os atributos do objeto depois que o objeto
    # for criado
    # pikachu.name = "Pikachu"
    # pikachu.type = "Elétrico"
    # pikachu.health = 70
    pikachu.info()

    pikachu.attack()
    pikachu.dodge()
    pikachu.evolve()

    pikachu.info()
