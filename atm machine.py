class ATM:
    def __init__(self):
        self.__pin = 1234

    def verify_pin(self, pin):
        if pin == self.__pin:
            print("Correct PIN")
        else:
            print("Wrong PIN")

    def change_pin(self, old, new):
        if old == self.__pin:
            self.__pin = new
            print("PIN Changed")

a = ATM()
a.verify_pin(1234)
a.change_pin(1234, 5678)