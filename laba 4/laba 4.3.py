from enum import Enum
class match(Enum):
    addition = 1
    subtraction = 2
    multiplication = 3
    division = 4
def num_match(firstNumber, secondNumber, operation):
    result = 0
    match operation:
        case match.addition:
            result = firstNumber + secondNumber
        case match.subtraction:
            result = firstNumber - secondNumber
        case match.multiplication:
            result = firstNumber * secondNumber
        case match.division:
            result = firstNumber / secondNumber
    return firstNumber, secondNumber, operation, result
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
operation = match[input("Enter the name of the operation: ")]
print(num_match(firstNumber, secondNumber, operation))