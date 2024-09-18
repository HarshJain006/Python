# exception_handling.py

"""
Exception Handling in Python

Exception handling is a mechanism to handle runtime errors, allowing the program to continue executing or to provide meaningful error messages. In Python, exceptions are handled using try, except, else, and finally blocks.

1. try block: The code that might cause an exception is placed inside the try block.
2. except block: This block will execute if an exception occurs in the try block.
3. else block: If no exception occurs in the try block, the code in the else block will execute.
4. finally block: This block will execute no matter if an exception occurs or not. It is typically used for clean-up actions.

Syntax:
try:
    # code that may raise an exception
except ExceptionType as e:
    # code that handles the exception
else:
    # code that runs if no exception occurred
finally:
    # code that runs regardless of whether an exception occurred or not
"""

# Example 1: Basic Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Example 2: Handling Multiple Exceptions
try:
    num = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Example 3: Using Else Block
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File opened successfully.")
    file.close()

# Example 4: Using Finally Block
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution completed.")

# Example 5: Custom Exception
class CustomError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise CustomError("Negative value not allowed!")

try:
    check_value(-1)
except CustomError as e:
    print(f"Custom Error: {e}")

"""
Assignments

1. **Assignment 1**: Handle the exception when dividing a number by zero. If an exception occurs, print "Cannot divide by zero".

2. **Assignment 2**: Write a program to handle multiple exceptions (IndexError and ValueError) when accessing elements in a list and converting a string to an integer.

3. **Assignment 3**: Create a program that opens a file. If the file does not exist, catch the exception and print an appropriate message. Ensure to close the file in a finally block.

4. **Assignment 4**: Write a program that takes user input and converts it to a float. Handle the exceptions if the input is not a valid number and print an error message.

5. **Assignment 5**: Define a custom exception called `NegativeValueError`. Write a function that raises this exception when a negative number is provided as input. Handle this exception in your code and print a message.

"""

# Solved Assignments

# Solved Assignment 1
try:
    num = 10
    divisor = 0
    result = num / divisor
except ZeroDivisionError:
    print("Cannot divide by zero")

# Solved Assignment 2
lst = [1, 2, 3]
try:
    index = 5
    item = lst[index]
except IndexError:
    print("Index out of range")

try:
    value = int("abc")
except ValueError:
    print("Invalid integer conversion")

# Solved Assignment 3
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("File not found")
finally:
    try:
        file.close()
    except NameError:
        pass  # File was never opened, so no need to close

# Solved Assignment 4
try:
    user_input = input("Enter a number: ")
    number = float(user_input)
except ValueError:
    print("Invalid input, not a number")

# Solved Assignment 5
class NegativeValueError(Exception):
    pass

def check_positive(value):
    if value < 0:
        raise NegativeValueError("Negative values are not allowed")

try:
    check_positive(-5)
except NegativeValueError as e:
    print(f"Negative Value Error: {e}")
