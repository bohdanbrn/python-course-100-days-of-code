import art

print(art.logo)

operations = {
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/"
}

def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    
def calculate_result(first_number, second_number, operation):
    result = calculate(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {result}") 

    return result

first_number = float(input("What's the first number?: "))

should_continue = True

while should_continue:
    print("+ \n- \n* \n/")
    operation = input("Pick an operation: ")

    if operation not in operations:
        print(f"Invalid operation - {operation}. Possible operations: {', '.join(operations.keys())}")
        break;

    second_number = float(input("What's your next number: "))
    result = calculate_result(first_number, second_number, operation)

    should_continue = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y"

    if should_continue:
        first_number = result
