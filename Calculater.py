num1 = int(input("Enter any number here: ")) # Get the first number from the user
num2 = int(input("Enter any number here: ")) # Get the second number from the user
operator = input("Which Operators do you want to use? +, -, /, *: ")# Get the operator from user
if operator == "+": # Check if the user choose "+"
  print(num1 + num2) # Print the sum of both numbers
elif operator == "-":# here it preforms "-"
  print(num1 - num2) # Print the difference of between the 2 numbers
elif operator == "/":# here if user chooses "/"
# here we used Nested condtion which means making sub conditions into conditions
  if num2 != 0:  # Check that the second number is not zero
    print(num1 / num2)# then it prints the division of number1 and number2
  else: 
    print("Cannot divide by zero!")# if second number equals to 0 then this one line will be printed
elif operator == "*": # here it performs "*"
  print(num1 * num2) # Print the product of the both nubmers
else:
  print("Try again!") # Print this message if the operator is invlaid
