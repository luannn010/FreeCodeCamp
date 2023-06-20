class Category:

  def __init__(self, name, fund=0):
    self.name = name
    self.fund = fund
    self.ledgerlist = []

  def deposit(self, amount, description):
    transaction = {"amount": amount, "description": description}
    self.fund += amount
    self.ledgerlist.append(transaction)

  def withdraw(self, amount, description=""):
    transaction = {"amount": f"-{amount}", "description": description}
    self.fund -= amount

    if self.fund < 0:
      self.fund += amount
      self.ledgerlist = self.ledgerlist
      return False
    self.ledgerlist.append(transaction)
    return True

  def get_balance(self):
    return f"Balance: {self.fund}"

  def transfer(self, amount, category):
    if self.withdraw(amount, f"Transfer to {category.name}"):
      category.deposit(amount, f"Transfered from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    if amount > self.fund:
      return False
    return True

  def __str__(self):
    max_length = 30
    first_line = adjust_first_line(self.name, max_length)
    transactions = middle_lines(self.ledgerlist, max_length)
    last_line = f"{self.fund}"
    return f"{first_line}\n{transactions}\n{last_line}"


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
    amount_str = amount[:7].rjust(7)  # Right-align amount to 7 characters
    description_str = description[:23].ljust(
      23)  # Left-align description to 23 characters
    trimmed_values = description_str + amount_str  # Combine description and amount strings
    result.append(
      trimmed_values.center(max_length))  # Center-align the combined string
  return "\n".join(result)


# def create_spend_chart(categories):
