# create a new input that takes an float (decimal number)
grossIncome = float(input("Enter your gross income: "))

# change the gross income to the net income using .0625
netIncome = grossIncome - (grossIncome * .0625)

# we need to ask for the users bills, but we also need to ask over and over again until the user terminates the loop using a -1
# this is just one way we can do this - this example below is using a While Loop Function
# this input is for your user to enter and start the bills loop function
bills = float(input("Please enter your first bill: "))

# we can use the sum variable to add our bills. This is stating that our sum variable will start at zero.
sum = 0
# we can use the count variable to add the number of input entries our user makes. This is stating that our count variable will start at zero.
count = 0

# while Loop Function Start - Everything in thing function will run in a loop until -1 is used to terminate the loop
while (bills != -1) :
  # we need to add the bills together
  sum += bills
  # we need to count the number of inputs the user is entering
  count += 1
  # we need the loop to prompt our user to enter another bill - we can copy/paste the whole bill variable line.
  bills = float(input("Please enter a bill: "))

# we need to print out all of our data in a presentable way so the user may view all information
print("Gross Income: " + str(grossIncome))
print("Net Income: " + str(netIncome))
print("Bills Total: " + str(sum))
print("Number of Bills Entered: " + str(count))

# last lines need to subtract the total bills from our netIncome and print the leftOverIncome
leftOverIncome = netIncome - sum
print("Your Usable Monthly Amount: " + str(leftOverIncome))
