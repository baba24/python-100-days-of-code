print("welcome to tip calculator")

total_bill = float(input("What was the total bill? $ "))

percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15 "))

num_total = int(input("How many people split the bill? "))

if percent_tip == 10:
    percent = (100 + percent_tip) / 100  * total_bill

elif percent_tip == 12:
    percent = (100 + percent_tip) / 100 * total_bill

else:
    percent = (100 + percent_tip) / 100 * total_bill

each_get =  round((percent / num_total),2)

print(f"each person should pay: ${each_get}")

print

