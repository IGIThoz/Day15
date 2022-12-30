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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "amount":0, # Edit resources
}


# TODO: 1 Prompt user by asking "What would you like? (espresso/latte/cappuccino):"

# TODO: 2 Turn off the Coffee Machine by entering “off” to the prompt.
#control = input("Turn off Coffee Machine. Type 'off'")
def off(value):
  """Using turn off Coffee Machine"""
  print("Coffee Manchine shutdown!")
  return value == "off"
# TODO: 3 Print report
def report():
  """Using print Report Coffee Machine"""
  print(f"water: {resources['water']}")
  print(f"milk: {resources['milk']}")
  print(f"coffee: {resources['coffee']}")
  print(f"amount: {resources['amount']}")
# TODO: 4 Check resources sufficient?
def resources_sufficient(coffee):
  
  # print(f"water: {resources['water']}")
  # print(f"milk: {resources['milk']}")
  # print(f"coffee: {resources['coffee']}")
  
  order = MENU[coffee]['ingredients']  
  for item in order:
    if order[item] > resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
    return True

# TODO: 5 Process coins.
  #def processcoins(quarters,dimes): 
  #  quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO: 6 Check transaction successful?
    
# TODO: 7 Make Coffee.
  
controlmanchine = {
 #"off": off,
 #"report": report,
  "espresso": resources_sufficient,
  "latte": resources_sufficient,
  "cappuccino":resources_sufficient,
}
# Run Machine 
  # Dùng dictionary để làm bộ câu lệnh
machine_off = False
while not machine_off:
  select = input("What would you like? (espresso/latte/cappuccino):") 
  
  if select in controlmanchine:
    drink = controlmanchine[select](select)
    
  elif select == "report":
    report()
  elif select =="off":
    machine_off = off(select)

# if select == "report":
#   report()
# elif select =="off":
#   print(off())
# elif select =="espresso" or select == "latte" or select == "cappuccino":
#   resources_sufficient()