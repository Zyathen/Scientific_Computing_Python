import math

# Objects added to the ledger, containing an amount and a description
class Category:
  #Initiate the object
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    budget = ""
    num_stars = 30 - len(self.name)
    budget += ("*" *
               (num_stars // 2)) + str(self.name) + ("*" *
                                                     (num_stars // 2)) + "\n"

    total = 0.00

    for obj in self.ledger:

      # Adding the description
      des_length = len(obj["description"])
      if des_length <= 23:
        budget += obj["description"] + ((23 - des_length) * " ")
      else:
        budget += obj["description"][:23] + " "

      # Adding the amount
      if obj["amount"] < 0:
        amount_length = 1
      else:
        amount_length = 0

      amount_length += len(str(obj["amount"]))
      if amount_length < 7:
        budget += ((6 - amount_length) * " ")
      budget += "{:.2f}\n".format(obj["amount"])

      total += obj["amount"]

    budget += "Total: {:.2f}".format(total)
    return budget

  # Creates an object and adds to ledger
  def deposit(self, amount, description=""):
    obj = {"amount": float(amount), "description": description}
    (self.ledger).append(obj)

  # Checks funds and processes the amount to withdraw, returns true if successful
  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      obj = {"amount": -float(amount), "description": description}
      (self.ledger).append(obj)
      return True
    return False

#Returns the current balance of the budget category based on ledger

  def get_balance(self):
    balance = 0.00
    for obj in self.ledger:
      balance += obj["amount"]
    return balance

#Adds a withdrawl from curr category and adds deposist in input category

  def transfer(self, amount, category):
    if self.check_funds(amount) == False:
      return False
    self.withdraw(amount, ("Transfer to " + category.name))
    category.deposit(amount, ("Transfer from " + self.name))
    return True

#If the amount is greater than the balance, will return false

  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    return True

#Takes a list of categories and returns a bar chart
def create_spend_chart(categories):
  bar_chart = "Percentage spent by category\n"
  # Calculating total_withdraws and withdraws from category
  total_withdraws = 0.00
  category_withdraws = []
  for category in categories:
    withdraw = 0.00
    for objs in category.ledger:
      if (objs["amount"] < 0):
        withdraw += (-1 * objs["amount"])
    category_withdraws.append((category.name, withdraw))
    total_withdraws += withdraw

  print("Total withdraw: " + str(total_withdraws))
  # Calculating the percentages for each category
  percentages = []
  for category in category_withdraws:
    percentage = ((category[1] / total_withdraws) * 100)
    percentage = math.ceil(percentage / 10) * 10
    percentages.append((category[0], percentage))

  # Printing the bars
  for i in reversed(range(0, 110, 10)):
    #Formatting for the y-axis
    if i == 0:
      bar_chart += "  {}| ".format(str(i))
    elif i == 100:
      bar_chart += str(i) + "| "
    else:
      bar_chart += " {}| ".format(str(i))

    # Printing the bars for each category
    for category in percentages:
      if category[1] > i:
        bar_chart += "o  "
      else:
        bar_chart += "   "
    bar_chart += "\n"

  bar_chart += "    " + ((len(percentages) * 3) + 1) * "-"

  # Print the category names
  num_categories = len(percentages)
  categories_completed = 0
  counter     = 0

  while categories_completed != num_categories:
    bar_chart += "\n     "
    for category in percentages:
      if len(category[0]) == counter:
        categories_completed += 1
      if len(category[0]) <= counter:
        bar_chart += "   "
      else:
        bar_chart += category[0][counter] + "  "

    counter += 1

  bar_chart = bar_chart.rstrip() + "  "
  return bar_chart