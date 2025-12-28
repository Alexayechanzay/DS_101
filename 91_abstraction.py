from abc import ABC,abstractmethod
class Price(ABC): # declare as abstract class
    def printSlip(self,amt):
        print(f"Payment amount: {amt}")

    @abstractmethod
    def payment(self):
        return 'Nothing from abstract method'

#p = Price() # cannot instantiate abstract class like this

class CreditCardPayment(Price):
    def payment(self, amount):
        print(f"Payment with Credit Card {amount}")

class MobileBanking(Price):
    def payment(self, amount):
        print(f"Payment with mobile banking {amount}")

o = MobileBanking()
o.printSlip(2000)
o.payment(2000)
