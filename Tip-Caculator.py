print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
percentTip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = totalBill * (percentTip / 100)

totalBillAfterTip = totalBill + tip

splitBill = round(totalBillAfterTip / people, 2)

print("Total is: $" + str(totalBillAfterTip))
print("Each person should pay: $" + str(splitBill))