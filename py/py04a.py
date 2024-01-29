num1 = int(input("Choose a number:"))
num2 = int(input("Choose another one:"))
operate = input(
    "Choose an operation:\n \tOptions are: +, -, * or /. \n \tWrite 'exit' to finish.")

while (operate != "exit"):
    if (operate == "+"):
        result = num1 + num2
    elif (operate == "-"):
        result = num1 - num2
    elif (operate == "*"):
        result = num1*num2
    elif (operate == "/"):
        result = num1/num2
    else:
        result = "Choose the right operation"

    print(result)

    num1 = int(input("Choose a number:"))
    num2 = int(input("Choose another one:"))
    operate = input(
        "Choose an operation:\n \tOptions are: +, -, * or /. \n \tWrite 'exit' to finish.")

else:
    exit(0)
