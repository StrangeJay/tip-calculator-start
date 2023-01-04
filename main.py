print("Welcome to the tip calculator") 

bill = float(input("What was the total bill? $")) 

percent = int(input("what percentage tip would you like to give? 10, 12 0r 15? ")) 

party = int(input("How many people to split the bill? "))  

tip = bill * (percent / 100) 

pay = (bill + tip) / party

# print(f"Each person should pay: ${round(pay, 2)}") 

# format and ensure it's set to 2 decimal places, even though it's not required
final_amount = "{:.2f}".format(pay) 

print(f"Each person should pay: ${final_amount}") 