
# Classe pai (ou super classe) responsável pelo pagamento
class Payment:

    def __init__(self, value):
        self._value = value

    def make(self):
        # Gera uma exceção de código não implementado.
        # Na prática, todas as classes que herdam da classe Payment
        # e que precisarem usar o método make, terão que implementar
        # esse método
        print("Você deve implementar esse método")


# Aqui criamos a classe BankslipPayment que herda as características
# da class Payment (métodos e atributos)
class BankslipPayment(Payment):
    pass
    # def make(self):
    #     print("Pagando")

if __name__ == '__main__':

    payment = Payment(10)
    bankslip_payment = BankslipPayment(10)
    bankslip_payment.make()
    print("ok")
