# Lambda Functions in Python

## 1. What is a Lambda Function?
# A lambda function is a small anonymous function defined using the `lambda` keyword.
# It can take any number of arguments but has only one expression.

# Syntax: lambda arguments: expression

# Example:
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5


## 2. Why Use Lambda Functions?
# Lambda functions are useful in cases where you need a small function for a short period of time and don't want to define a separate function using `def`.
# They're often used with functions like `map()`, `filter()`, and `sorted()`.

# Example using lambda with `sorted()`:
points = [(1, 2), (3, 1), (5, -1), (0, 0)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)  # Output: [(5, -1), (0, 0), (3, 1), (1, 2)]


## 3. Using Lambda with map()
# The `map()` function applies a function to all items in an input list.

# Example:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]


## 4. Using Lambda with filter()
# The `filter()` function filters elements in a sequence based on a condition.

# Example:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


## 5. Using Lambda with reduce()
# The `reduce()` function is used to apply a function cumulatively to the items in a sequence, reducing it to a single value.
# `reduce()` is available in the `functools` module.

from functools import reduce

# Example:
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120


## 6. Lambda Function with Multiple Arguments
# Lambda functions can take multiple arguments, and their use cases extend beyond basic arithmetic.

# Example:
max_value = lambda a, b, c: max([a, b, c])
print(max_value(10, 20, 5))  # Output: 20


## 7. Lambda with Conditional Statements
# You can include conditions within lambda functions using ternary operators.

# Example:
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))  # Output: 20


# Solved Assignments

# Assignment 1: Write a lambda function to find the cube of a given number.

cube = lambda x: x ** 3
print(cube(3))  # Output: 27


# Assignment 2: Use lambda and `map()` to convert a list of temperatures in Celsius to Fahrenheit.

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]


# Assignment 3: Use lambda and `filter()` to filter out words that are shorter than 4 characters from a list of strings.

words = ['apple', 'bat', 'cat', 'elephant', 'dog']
long_words = list(filter(lambda word: len(word) >= 4, words))
print(long_words)  # Output: ['apple', 'elephant']


# Assignment 4: Use lambda and `reduce()` to find the product of all numbers in a list.

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24


# Assignment 5: Write a lambda function to check if a string is a palindrome.

is_palindrome = lambda s: s == s[::-1]
print(is_palindrome('radar'))  # Output: True
print(is_palindrome('hello'))  # Output: False

