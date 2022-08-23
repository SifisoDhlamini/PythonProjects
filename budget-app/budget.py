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
    width = len(categories) * 3
    longest_word = max(len(category.name) for category in categories)
    height = 11 + 1 + longest_word
    percentages = {"100": "", "90": "", "80": "", "70": "", "60": "",
                   "50": "", "40": "", "30": "", "20": "", "10": "", "0": ""}
    for category in categories:
        percentage = calc_percentage(category)
        while percentage in percentages:
            percentages[percentage] += "o  "
            percentage = str(int(percentage) - 10)

    divider = ("-" * (width - 4) + "\n").rjust(width)
    header = f"Percentage spent by category\n"
    names = []
    for i in range(0, longest_word):
        name = " " * 5
        for category in categories:
            if i < len(category.name):
                name += category.name[i] + "  "
            else:
                name += "   "
        names.append(name)
    names = "\n".join(names)
    chart = []
    for percentage in percentages:
        prefix = f"{percentage}".rjust(3)
        postfix = f"{percentages[percentage]}".ljust(width, " ")
        chart.append(f"{prefix}| {postfix}")
    chart = "\n".join(chart)
    return header + chart + '\n' + divider + names


def greater_than_zero(entry):
    return entry["amount"] > 0


def calc_percentage(category):
    total_deposited = 0
    for transaction in category.ledger:
        if transaction["amount"] > 0:
            total_deposited += transaction["amount"]
    total_spent = total_deposited - category.get_balance()
    percentage = total_spent / total_deposited * 100
    return str(int((percentage // 10) * 10))
