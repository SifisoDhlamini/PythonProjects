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
        withdrew = self.withdraw(
            amount, "Transfer to {}".format(category.name))
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
            transactions.append(
                f"{description.ljust(30-right)}{amount.rjust(right)}\n")
        transactions = "".join(transactions)
        total = f"Total: {self.get_balance():.2f}"

        return title + transactions + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    percentages = range(100, -10, -10)
    total_spending = 0
    spendings = {}
    for category in categories:
        spent = 0
        cat_name = category.name
        for entry in category.ledger:
            if entry["amount"] < 0:
                spent += abs(entry["amount"])
        spendings[cat_name] = spent
        total_spending += spent
    spent_percentages ={}
    for cat_name, spent in spendings.items():
        percentage = spent / total_spending * 100
        spent_percentages[cat_name] = percentage

    for percentage in percentages:
        chart += f"{percentage}".rjust(3) + "| "
        for category in categories:
            if spent_percentages[category.name] >= percentage:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    width = len(categories) * 3 + 5
    divider = ("-" * (width - 4)).rjust(width)
    chart += divider + "\n"

    names = []
    longest_name_length = max(len(category.name) for category in categories)
    for i in range(0, longest_name_length):
        name = " " * 5
        for category in categories:
            if i < len(category.name):
                name += category.name[i] + "  "
            else:
                name += "   "
        names.append(name)
    names = "\n".join(names)
    chart += names
    return chart

    


