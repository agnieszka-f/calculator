import sys
import logging
logging.basicConfig(level=logging.DEBUG)

actions = {
  1 : ("Dodaje", lambda a, b : a + b),
  2 : ("Odejmuje", lambda a, b : a - b),
  3 : ("Mnoże", lambda a, b : a * b),
  4 : ("Dziele", lambda a, b : a/b)
}

def get_proper_value(message):
  value = None
  while value == None:
   input_value = input(message)
   if input_value.isnumeric():
      value = int(input_value)
   else:
     logging.warning("Podałeś/aś niepoprawną wartość.")
  return value  

action_type = 0
while action_type < 1 or action_type > 4:
   action_input = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
   is_numeric = action_input.isnumeric()
   if is_numeric:
      action_type = int(action_input)  
   if is_numeric == False or (action_type < 1 or action_type > 4):
      logging.warning("Podałeś/aś niepoprawną wartość.")

number_a  = get_proper_value("Podaj składnik 1: ")
number_b =  get_proper_value("Podaj składnik 2: ")

logging.info(f"{actions.get(action_type)[0]} {number_a} i {number_b}")

result = actions.get(action_type)[1](number_a, number_b)

logging.info(f"Wynik to {result}")
