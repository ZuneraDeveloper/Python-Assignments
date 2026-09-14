menu = ("=" * 40 + "\n Welcome to the calculator \n 1.Addition \n 2. Substration\n 3. Multiply \n 4. Division \n 5. Exit \n" + "=" * 40)

choice = 0

while choice != 5:

    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("The sum of ",num1,"and",num2,"is :", num1 + num2)

    elif choice ==2:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("The substration of ",num1,"and",num2,"is :",num1 - num2)

    elif choice == 3:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("The multiplication of", num1,"and", num2,"is :",num1 * num2)

    elif choice == 4:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        if num2 != 0:
            print("The division of", num1,"and", num2,"is :",num1 / num2)
        else:
            print("Cannot divide by zero!")

    elif choice == 5:
        print("Exiting the calculator. Goodbye!")

    else:
        print("Your entered an Invalid number. \n Please try again!")
