import uuid
from random import randint

# Foi usada a primeira aula de banco de dados para
# finalizar o assunto de orientação a objetos
# herança, polimorfismo e composição


# Classe pai (ou super classe) responsável pelo pagamento
class Payment:

    # Quanto instanciamos a classe, o método __init__ é chamado
    def __init__(self, value):
        # Estamos criando o atributo _value do objeto e atribuindo
        # o valor recebido no argumento value
        self._value = value

    # Método responsável por realizar o pagamento
    def make(self):
        # Gera uma exceção de código não implementado.
        # Na prática, todas as classes que herdam da classe Payment
        # e que precisarem usar o método make, terão que implementar
        # esse método
        print("Você deve implementar esse método")


# Aqui criamos a classe BankslipPayment que herda as características
# da class Payment (métodos e atributos)
class BankslipPayment(Payment):

    def make(self):
        output = f"""
        O boleto {str(uuid.uuid4())} foi pago no valor de {self._value}
        """

        print(output)


class CreditCardPayment(Payment):
    def __init__(self, value, number, code):

        # Utilizando a função built-in super() conseguimos acessar os métodos ou
        # atributos definidos na classe pai
        super().__init__(value)
        self._number = number
        self._code = code

    def _credit_card_is_valid(self):
        return bool(randint(0, 1))

    def make(self):
        if self._credit_card_is_valid():
            output = f"""
            Dados de pagamento via cartão
            Valor: {self._value}
            Número: {self._number}
            Código: {self._code}
            """

            print(output)
        else:
            print("Não foi possível realizar o pagamento com o cartão")


"""
Vai receber 3 argumentos: valor, agencia e numero da conta bancaria
Terá um método privado que vai retornar se o usuário tem saldo ou não
"""
class BankTransferPayment(Payment):

    def __init__(self, value, agency, account):
        super().__init__(value)
        self._agency = agency
        self._account = account

    def _has_balance(self):
        return bool(randint(0, 1))

    def make(self):
        if self._has_balance():
            output = f"""
            Dados de pagamento:
            
            Valor: {self._value}
            Agência: {self._agency}
            Conta: {self._account}
            """

            print(output)
        else:
            print("Você não tem saldo para realizar essa transferência")


if __name__ == '__main__':

    # payment = Payment(10)
    bankslip_payment = BankslipPayment(199.50)
    # bankslip_payment.make()

    credit_card_payment = CreditCardPayment(201, "8345-0923-4981-0985", "123")
    # credit_card_payment.make()

    bank_transfer_payment = BankTransferPayment(500, "890456-2", "12345")
    # bank_transfer_payment.make()

    for payment_type in [bankslip_payment, credit_card_payment, bank_transfer_payment]:
        payment_type.make()

# Pesquisar sobre herança múltipla, MRO, Mixins