MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 50000,
    "milk": 20000,
    "coffee": 10000,
}
revenue = 0

# TODO: 2 Turn off the Coffee Machine by entering “off” to the prompt.
def off(value):
  """Using turn off Coffee Machine"""
  print("Coffee Manchine shutdown!")
  return value == "off"
# TODO: 3 Print report
def report():
  """Using print Report Coffee Machine"""
  global revenue
  print(f"water: {resources['water']} ml")
  print(f"milk: {resources['milk']} ml")
  print(f"coffee: {resources['coffee']} ml")
  print(f"amount: ${revenue}")
  
# TODO: 4 Check resources sufficient?
def resources_sufficient(coffee):
  order = MENU[coffee]['ingredients']  
  for item in order:
    if order[item] > resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
    return True

# TODO: 6 Check transaction successful?
def transaction(coffee,amount):
  cost = MENU[coffee]['cost']
  if cost > amount:
    print("Sorry that's not enough money. Money refunded")
    print(amount)
    return False  
  return True
# TODO: 7 Make Coffee.
def make_coffee(coffee,amount):
  order = MENU[coffee]['ingredients']  
  for item in order:
    resources[item] = resources[item] - order[item]
  revenue = MENU[coffee]['cost']
  repayment = round(amount - MENU[coffee]['cost'],2)
  print(f"Here is ${repayment} in change.")
  print( "Here is your latte. Enjoy")
  return revenue

#Control manchine  
controlmanchine = {
  "espresso": resources_sufficient,
  "latte": resources_sufficient,
  "cappuccino":resources_sufficient,
}
# Run Machine 
def coffee_machine():
  coins = 0
  machine_off = False
  while not machine_off
  # TODO: 1 Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    select = input("What would you like? (espresso/latte/cappuccino):") 
    
    if select in controlmanchine:
      drink = controlmanchine[select](select)
      if drink == True:
        # TODO: 5 Process coins.
        coins += float(input("quarters:")) * 0.25
        coins += float(input("dimes:")) * 0.1
        coins += float(input("nickles:")) * 0.05
        coins += float(input("pennies:")) * 0.01
        if transaction(select,coins) == True:
           amount = make_coffee(select,coins)
           global revenue
           revenue += amount
    elif select == "report":
      report()
    elif select =="off":
      machine_off = off(select)

coffee_machine()