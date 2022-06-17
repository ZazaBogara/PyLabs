class Accounting:
    def __init__(self, name: str, amount: int, price: float):
        self.name = name
        self.amount = amount
        self.price = price
    def show(self):
        print(self.name,self.amount,self.price)
class Stuff(Accounting):
    def __init__(self, name: str, amount: int, price: float, is_on_storage: bool):
        super().__init__(name,amount,price)
        self.is_on_storage = is_on_storage
    def show(self):
        print(self.name,self.amount,self.price,self.is_on_storage)
class Buyer(Stuff):
    def __init__(self, name: str, stuffs: list()):
        self.name = name
        self.storage = stuffs
    def show(self):
        for i in self.storage:
            i.show()