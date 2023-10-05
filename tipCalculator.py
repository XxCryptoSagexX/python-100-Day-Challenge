#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calulator.")
total_bill = input("What was the total bill? $")
percentage_tip = input(
    "what percentage tip would you like to give? 10, 12, or 15? ")
party_size = input("How many people will split the bill? ")
# TO DO

def tipCalculator(bill, percentage, party):
    bill_value = float(bill)
    percent_value = int(percentage) / 100
    party_value = int(party)

    tipcalc = bill_value * (1 + percent_value) / party_value
    return float(tipcalc)

result = tipCalculator(total_bill, percentage_tip, party_size)
rounded_result = round(result, 2)
rounded_result = "{:.2f}".format(result)  #expected to google this part.
print("Each pershon should pay: $" + str(rounded_result))