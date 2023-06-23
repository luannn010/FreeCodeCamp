class Category:

  def __init__(self, name, fund=0):
    self.name = name
    self.fund = fund
    self.ledger = []

  def deposit(self, amount, description=""):
    transaction = {"amount": amount, "description": description}
    self.fund += amount
    self.ledger.append(transaction)

  def withdraw(self, amount, description=""):
    transaction = {"amount": -amount, "description": description}
    self.fund -= amount

    if self.fund < 0:
      self.fund += amount
      self.ledger = self.ledger
      return False
    self.ledger.append(transaction)
    return True

  def get_balance(self):
    return self.fund

  def transfer(self, amount, category):
    if self.withdraw(amount, f"Transfer to {category.name}"):
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    if amount > self.fund:
      return False
    return True

  def __str__(self):
    max_length = 30
    first_line = adjust_first_line(self.name, max_length)
    transactions = middle_lines(self.ledger, max_length)
    last_line = f"{self.fund}"
    return f"{first_line}\n{transactions}\nTotal: {last_line}"


def adjust_first_line(name, max_length):
  line = "*" * max_length
  half_length = len(name) // 2
  start_index = max_length // 2 - half_length
  prefix = line[:start_index]
  suffix = line[start_index + len(name):]
  new_line = prefix + name + suffix
  return new_line


def middle_lines(transactions, max_length):
  result = []
  for transaction in transactions:
    amount = str(transaction.get("amount", ""))
    description = str(transaction.get("description", ""))
    amount_str = f"{transaction['amount']:7.2f}"  # Right-align amount to 7 characters
    description_str = description[:23].ljust(23)  # Left-align description to 23 characters
    trimmed_values = description_str + amount_str  # Combine description and amount strings
    result.append(
      trimmed_values.center(max_length))  # Center-align the combined string
  return "\n".join(result)


def create_spend_chart(categories):
    category_names = []
    category_spent = []
    total_spent = 0

    for category in categories:
        name = category.name
        spent = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                spent -= transaction["amount"]
        category_names.append(name)
        category_spent.append(spent)
        total_spent += spent

    percentages = [(spent / total_spent) * 100 if total_spent > 0 else 0 for spent in category_spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart

