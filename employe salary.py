class Employee:
    def __init__(self):
        self.__salary = 30000

    def get_salary(self):
        print(self.__salary)

    def set_salary(self, salary):
        self.__salary = salary

e = Employee()
e.get_salary()
e.set_salary(50000)
e.get_salary()