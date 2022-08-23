class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []    

    def get_balance(self):
        return sum(entry["amount"] for entry in self.ledger)
    
    def check_funds(self, amount):
        return self.get_balance() >= amount
    
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

    def __str__(self) -> str:
        title = f"{self.name.center(30, '*')}\n"
        transactions = []
        for transaction in self.ledger:
            amount = "{:.2f}".format(transaction["amount"])
            right = len(str(amount)) + 1
            description = transaction["description"][:30 - right]
            transactions.append(f"{description.ljust(30-right)}{amount.rjust(right)}\n")
        transactions = "".join(transactions)     
        total = f"Total: {self.get_balance():.2f}"

        return title + transactions + total
        


def create_spend_chart(categories):
    ...
    
