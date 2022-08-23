class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    @property
    def get_balance(self):
        return sum(entry["amount"] for entry in self.ledger)
    
    def check_funds(self, amount):
        return self.balance >= amount
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False    
    
    def transfer(self, amount, category):
        withdrew = self.withdraw(amount, "Transfer to {}".format(category.name))
        if withdrew:
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False


def create_spend_chart(categories):
    ...
