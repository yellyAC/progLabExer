while True:
    print("====ENTER TWO NUMBERS THAT YOU WANT TO PLUS, SUBRACT, MULTIPLY OR DIVIDE====")
    print("Enter first number: ")
    num1 = int(input())
    print("Enter Second Number: ")
    num2 = int(input())

    print("Select Operation: \n 1. Addition \n 2. Subraction \n 3. Multiplication \n 4. Division")
    print("Enter choice: ")
    choice = int(input())

    if choice == 1:
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == 2:
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == 3:
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == 4:
        print(num1, "/", num2, "=", num1 / num2)
    else:   
        print("Invalid Input") 

    try_again = input("Do you want to try again?[y / n]: ")
    if try_again == "n":
        break