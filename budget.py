class Category():

  def __init__(self,category_name):
    self.category_name = category_name.capitalize()
    self.ledger = []
    self.fund = 0
    self.total_withdrawal = 0

  def deposit(self,amount,description = ""):
    self.deposit_amount = amount
    self.deposit_description = description
    self.fund += self.deposit_amount
    self.ledger.append({"amount": self.deposit_amount,"description": self.deposit_description})

  def withdraw(self,amount,description=""):
    self.withdraw_amount = amount
    self.withdraw_description = description

    if self.check_funds(self.withdraw_amount):
      self.ledger.append({"amount": -self.withdraw_amount,"description": self.withdraw_description})
      self.fund -= self.withdraw_amount
      self.total_withdrawal += self.withdraw_amount
      return True

    else:
      return False

  def get_balance(self):
    
    return self.fund

  def transfer(self,amount,category):
    self.transfer_amount = amount
    self.category = category

    if self.check_funds(self.transfer_amount):
      self.withdraw(self.transfer_amount,"Transfer to "+(self.category.category_name))
      self.category.deposit(self.transfer_amount,"Transfer from "+(self.category_name))
      return True

    else:
      return False

  def check_funds(self,amount):
    self.amount = amount
    return (self.amount <= self.get_balance())

  def __str__(self):
    item_line = ""
    title_line = ((self.category_name.capitalize()).center(30,"*"))
    
    for i in range(len(self.ledger)):
      
      temp_line_1 = (self.ledger[i].get("description"))[:23]
      temp_line_2 = str(format((self.ledger[i].get("amount")),".2f")).rjust(30 - len(temp_line_1))
      item_line += (temp_line_1) + temp_line_2 + "\n"
      
    total_line = f"Total: {self.get_balance()}"

    return (title_line + "\n" + item_line + total_line)

def create_spend_chart(categories):

  withdrawal = [categories[w].total_withdrawal for w in range(len(categories))]
  withdrawal_percentage = [round((withdrawal[i]/sum(withdrawal))*100) for i in range(len(withdrawal))]

  title_line = "Percentage spent by category\n"
  bar_chart_line = ""

  for i in range(100,-10,-10):
    bar_chart_line += ((str(i)+"|").rjust(4))
    for j in range(len(withdrawal_percentage)):
      if withdrawal_percentage[j] >= i:
        bar_chart_line += " o "
      else:
        bar_chart_line += "   "
    bar_chart_line += " \n"
  bar_chart_line += ("-"*((len(categories)*3)+1)).rjust((len(categories)*3)+5) + "\n"

  category_line = ""
  for i in range(max([len(c.category_name) for c in categories])):
    category_line += "    "
    for j in range(len(categories)):
      if i < len(categories[j].category_name):
        category_line += " "+ categories[j].category_name[i] + " "
      else:
        category_line += "   "
    category_line += " \n"
   
  return (title_line + bar_chart_line + category_line).rstrip("\n")