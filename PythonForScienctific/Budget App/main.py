from category import Category

def main():
    
    # Create instances of the Category class
    category1 = Category("Food")
    category2 = Category("Clothing")

    # Deposit money to category1
    category1.deposit(200, "Groceries")
    category1.deposit(300, "Restaurant")

    # Withdraw money from category1
    category1.withdraw(100, "Snacks")

    # Transfer money from category1 to category2
    category1.transfer(150, category2)

    # Print the categories
    print(category1)
    print(category2)


if __name__ == "__main__":
    main()
