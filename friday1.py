def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return "error"


def is_whole_number(num1):
    return num1 % 1 == 0


result = 0

operation = input("What sort of operation do you want to perform? Enter + , - , * , or / . ").strip()
first_number = float(input("Enter the first number in the equation. "))
second_number = float(input("Enter the second number in the equation. "))

if operation == "+":
    result = addition(first_number, second_number)
elif operation == "-":
    result = subtraction(first_number, second_number)
elif operation == "*":
    result = multiplication(first_number, second_number)
elif operation == "/":
    result = division(first_number, second_number)
else:
    print ("You didn't enter a valid operator!")
    result = "error"  # No result if operation is invalid

if result == "error":
    print("Your request is invalid. Sorry!")
else:
    if is_whole_number(first_number):
        first_number = int(first_number)
    if is_whole_number(second_number):
        second_number = int(second_number)
    if is_whole_number(result):
        result = int(result)

    print(f"{first_number} {operation} {second_number} = {result}.")
    print(test_values)
