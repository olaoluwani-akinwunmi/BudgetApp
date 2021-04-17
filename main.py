import budgetapp

food=budgetapp.Budget("Food")
clothing=budgetapp.Budget("Clothing")
entertainment=budgetapp.Budget("Entertainment")


food.deposit(1000, "Deposit")
food.withdraw(100.5, "Vegetable")
food.transfer(500, clothing)


clothing.deposit(5000, "Deposit")
clothing.withdraw(200, "Jeans")
clothing.withdraw(130, "Ray Ban")


entertainment.deposit(2500, "Deposit")
entertainment.transfer(30, food)
entertainment.withdraw(1000, "Netflix")


print(food)
print(clothing)
print(entertainment)