print("this project taking about organizing your monthly and yearly salary made by :rafael moheb,aser monhamed and karras joseph")

user_mory = input("Enter you need to organizing your monthly salary or yearly: ")

if user_mory=="monthly":
  user_mory2 = input("you need to enter the price of things bay in the month one by one or all: ")
  total_buy = 0

  if user_mory2 == "one by one":
    number1 = int(input("Enter number of things you need: "))
    for j in range(number1):
      price = int(input("Enter price of thing: "))
      total_buy += price

  elif user_mory2 == "all":
    total_buy = int(input("Enter total price for all things you need in month: "))

  if user_mory2 in ["one by one", "all"]:
    user_family = int(input("How many old persons: "))
    print("if you donot give your sons expenses enter 0 sons")
    user_family2 = int(input("How many sons: "))
    user_money = int(input("How much money did you get: "))

    if user_family > 0:
      print("per old person:", (total_buy - user_money) / user_family )
      print("your sons will get in the month", (total_buy - user_money) / user_family / 31)
      print("your sons will get in the day", (total_buy - user_money) / user_family / 31 / 24)
    else:
      print("Total expenses:", total_buy)

elif user_mory == "yearly":
  user_money2 = int(input("Enter your monthly salary: "))
  print("this is your yearly salary",user_money2*12)
  user_trips = int(input("when you go on trip haw mutch money did you spend: "))
  number2 =(input("you need to enter the price of things bay in the month one by one or all: "))
  total_buy2 = 0
  if number2 == "one by one":
     number3 = int(input("Enter number of things you need: "))
     for j in range(number3):
       price2 = int(input("Enter price of thing you need in month: "))
       total_buy2 += price2
       
  user_family3 = int(input("How many old persons: "))
  print("if you donot give your sons expenses enter 0 sons")
  user_family4 = int(input("How many sons: "))

  print("per old person will have in the year:",(user_money2*12 - user_trips - price2) / user_family3 )
  print("per old person will have in the month:",(user_money2*12 - user_trips - price2) / user_family3 / 31 )
  print("your sons will have in the year", (user_money2*12 - user_trips - price2) / user_family4 / 356.3 )
  print("your sons will have in the month", (user_money2*12 - user_trips - price2) / user_family4 / 31 / 356.3)

  if number2 == "all":
    price3 = int(input("Enter total price for all things you need in month: "))
    user_family5 = int(input("How many old persons: "))
    print("if you donot give your sons expenses enter 0 sons")
    user_family6 = int(input("How many sons: "))

    print("per old person will have in the year:",(user_money2*12 - user_trips - price3) / user_family5 )
    print("per old person will have in the month:",(user_money2*12 - user_trips - price3) / user_family5 / 31 )
    print("your sons will have in the year", (user_money2*12 - user_trips - price3) / user_family6 / 356.3)
    print("your sons will have in the month", (user_money2*12 - user_trips - price3) / user_family6 / 31 / 356.3)
  
else:
  print("Invalid option ✘. Please enter 'monthly' or 'yearly'.")