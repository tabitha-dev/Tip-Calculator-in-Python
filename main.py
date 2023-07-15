import os


def calculate_tip(bill_amount, tip_percentage):
  tip_amount = bill_amount * (tip_percentage / 100)
  return tip_amount


def calculate_total_bill(bill_amount, tip_amount):
  total_amount = bill_amount + tip_amount
  return total_amount


def calculate_amount_per_person(total_amount, num_people):
  amount_per_person = total_amount / num_people
  return amount_per_person


def validate_percentage_input(user_input):
  try:
    tip_percentage = float(user_input)
    if 0 <= tip_percentage <= 100:
      return True
  except ValueError:
    pass
  return False


def validate_people_input(user_input):
  try:
    num_people = int(user_input)
    if 1 <= num_people <= 1000:
      return True
  except ValueError:
    pass
  return False


def get_currency_symbol():
  while True:
    currency_symbol = input("Enter the currency symbol you want to use: ")
    if len(currency_symbol.strip()) == 1:
      return currency_symbol
    else:
      print(
        "Invalid input. Please enter a single character for the currency symbol."
      )


def format_amount(amount):
  formatted_amount = "{:,.2f}".format(round(amount, 2))
  return formatted_amount


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


def split_bill_evenly(total_amount, num_people):
  amount_per_person = total_amount / num_people
  return amount_per_person


def apply_round_up(tip_amount):
  rounded_tip_amount = round(tip_amount)
  return rounded_tip_amount


def apply_discount(bill_amount, discount_percentage):
  discount = bill_amount * (discount_percentage / 100)
  discounted_bill_amount = bill_amount - discount
  return discounted_bill_amount


def display_history(history):
  if not history:
    print("No previous calculations found.")
  else:
    print("\n----------------------------------------")
    print("          CALCULATION HISTORY           ")
    print("----------------------------------------")
    for index, calculation in enumerate(history, start=1):
      print(f"Calculation {index}:")
      print(f"Bill amount:         ${calculation['bill_amount']:.2f}")
      print(f"Tip percentage:      {calculation['tip_percentage']}%")
      print(f"Number of people:    {calculation['num_people']}")
      print(f"Total amount:        ${calculation['total_amount']:.2f}")
      print("----------------------------------------")


history = []

print("Welcome to the Tip Calculator!")

while True:
  try:
    bill_amount = float(input("Please enter the total bill amount: $"))

    while True:
      tip_percentage = input(
        "What percentage tip would you like to give? Enter a number: ")
      if validate_percentage_input(tip_percentage):
        tip_percentage = int(tip_percentage)
        break
      else:
        print("Invalid input. Please enter a valid tip percentage.")

    while True:
      num_people = input("How many people are splitting the bill? ")
      if validate_people_input(num_people):
        num_people = int(num_people)
        break
      else:
        print("Invalid input. Please enter a valid number of people.")

    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_amount = calculate_total_bill(bill_amount, tip_amount)
    amount_per_person = calculate_amount_per_person(total_amount, num_people)

    currency_symbol = get_currency_symbol()

    clear_screen()

    print("\n----------------------------------------")
    print("          TIP CALCULATOR RESULT          ")
    print("----------------------------------------")
    print(f"Total bill amount:         {currency_symbol}{bill_amount:.2f}")
    print(f"Tip percentage:            {tip_percentage}%")
    print(f"Number of people:           {num_people}")
    print("----------------------------------------")
    print(f"Tip amount:                {currency_symbol}{tip_amount:.2f}")
    print(f"Total bill with tip:       {currency_symbol}{total_amount:.2f}")
    print(
      f"Amount per person:         {currency_symbol}{format_amount(amount_per_person)}"
    )
    print("----------------------------------------")

    print(
      f"Each person should pay:     {currency_symbol}{format_amount(amount_per_person)}"
    )

    while True:
      additional_options = input("Do you want to do any of the following?\n"
                                 "1. Split the bill evenly\n"
                                 "2. Round up the tip amount\n"
                                 "3. Apply discount to the bill amount\n"
                                 "4. View calculation history\n"
                                 "5. None\n"
                                 "Enter your choice (1/2/3/4/5): ")

      if additional_options == "1":
        amount_per_person = split_bill_evenly(total_amount, num_people)
        print(
          f"Amount per person (evenly split): {currency_symbol}{format_amount(amount_per_person)}"
        )
      elif additional_options == "2":
        tip_amount = apply_round_up(tip_amount)
        total_amount = calculate_total_bill(bill_amount, tip_amount)
        amount_per_person = calculate_amount_per_person(
          total_amount, num_people)
        print(
          f"Updated tip amount (rounded up): {currency_symbol}{tip_amount:.2f}"
        )
        print(
          f"Updated total bill with tip:    {currency_symbol}{total_amount:.2f}"
        )
        print(
          f"Updated amount per person:      {currency_symbol}{format_amount(amount_per_person)}"
        )
      elif additional_options == "3":
        discount_percentage = float(input("Enter the discount percentage: "))
        bill_amount = apply_discount(bill_amount, discount_percentage)
        total_amount = calculate_total_bill(bill_amount, tip_amount)
        amount_per_person = calculate_amount_per_person(
          total_amount, num_people)
        print(
          f"Updated bill amount (discount applied): {currency_symbol}{bill_amount:.2f}"
        )
        print(
          f"Updated total bill with tip:           {currency_symbol}{total_amount:.2f}"
        )
        print(
          f"Updated amount per person:             {currency_symbol}{format_amount(amount_per_person)}"
        )
      elif additional_options == "4":
        display_history(history)
      elif additional_options == "5":
        break
      else:
        print("Invalid input. Please enter a valid option.")

    while True:
      another_calculation = input(
        "Do you want to calculate another tip? (yes/no) ")
      if another_calculation.lower() in ["yes", "no"]:
        break
      else:
        print("Invalid input. Please enter 'yes' or 'no'.")

    if another_calculation.lower() == "no":
      break

    history.append({
      "bill_amount": bill_amount,
      "tip_percentage": tip_percentage,
      "num_people": num_people,
      "total_amount": total_amount
    })

  except ValueError:
    print("Invalid input. Please enter a valid number for the bill amount.")
