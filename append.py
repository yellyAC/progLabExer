def inputValue():
    value_list = []
    try:
        print("Select an Operator")
        print("  (1) add (2) subtract: ")
        choice = int(input())

        count = int(input("Enter how many values: "))
        for i in range(count):
            value = int (input(f"value {i+1}: "))
            value_list.append(value)
    except:
            print("Input invalid. try again")
            return inputValue()
    return value_list
    
def mulitply(value):
    product = 1
    for i in value:
        product *= 1
    return product

value_list = inputValue()
answer = mulitply(value_list)
print(value_list)
print("Answer: ", answer)