class UPIPayment:
    def pay(self):
        print("Paid using UPI")

class CardPayment:
    def pay(self):
        print("Paid using Card")

class CashPayment:
    def pay(self):
        print("Paid using Cash")

u = UPIPayment()
c = CardPayment()
ca = CashPayment()

u.pay()
c.pay()
ca.pay()