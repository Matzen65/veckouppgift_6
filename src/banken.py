# 3 Banken
# Skapa en klass som representerar ett bankkonto. Banken ska kunna:
# sätta in pengar (deposit)
# ta up pengar (withdraw)
# returnera nuvarande saldo (balance)
# räkna ut ränta (apply_interest, lägger till räntan till kontot)
# tala om ifall man har råd att betala en räkning (returnera True/False)
#Gör en metod för varje funktion.
#Skriv enhetstester för varje funktion.


class Account:

    def __init__(self, savings = 0):
        self.__savings = savings

    def deposit(self, cash):
        self.__savings += cash

    def withdraw(self, cash):
        self.__savings -= cash

    def balance(self):
        return self.__savings

    def apply_interest(self, interest = 0.05):
        return self.__savings * (1 + interest)

    def afford(self, cost):
        return cost <= self.__savings


