# -------------------------------
# Python Dictionary Code Snippets
# -------------------------------

# 1. Creating Dictionaries
empty_dict = {}  # Empty dictionary
dict_with_values = {"apple": 2, "banana": 5, "orange": 3}  # Dictionary with initial key-value pairs
nested_dict = {"fruits": {"apple": 2, "banana": 5}, "vegetables": {"carrot": 10, "spinach": 15}}  # Nested dictionary

# 2. Accessing Dictionary Elements
print(dict_with_values["apple"])  # Access value by key
# Using get() method to access value
print(dict_with_values.get("banana"))  # Returns value if key exists
print(dict_with_values.get("grapes", "Key not found"))  # Returns default message if key doesn't exist

# 3. Adding and Updating Dictionary Elements
dict_with_values["grapes"] = 10  # Adding a new key-value pair
dict_with_values["apple"] = 6  # Updating an existing key's value
print(dict_with_values)

# 4. Removing Elements from a Dictionary
removed_value = dict_with_values.pop("orange")  # Removes the key and returns its value
print(f"Removed value: {removed_value}")
del dict_with_values["banana"]  # Removes the key-value pair
print(dict_with_values)
dict_with_values.clear()  # Clears the entire dictionary
print(dict_with_values)

# 5. Looping through Dictionaries
sample_dict = {"name": "John", "age": 25, "city": "New York"}

# Loop through keys
for key in sample_dict:
    print(f"Key: {key}")

# Loop through values
for value in sample_dict.values():
    print(f"Value: {value}")

# Loop through key-value pairs
for key, value in sample_dict.items():
    print(f"Key: {key}, Value: {value}")

# 6. Dictionary Methods
sample_dict = {"a": 1, "b": 2, "c": 3}

# Using keys(), values(), and items() methods
print(sample_dict.keys())  # Returns dictionary keys
print(sample_dict.values())  # Returns dictionary values
print(sample_dict.items())  # Returns dictionary key-value pairs

# Using update() method to merge dictionaries
additional_dict = {"d": 4, "e": 5}
sample_dict.update(additional_dict)
print(sample_dict)

# 7. Dictionary Comprehension
squared_dict = {x: x**2 for x in range(1, 6)}  # Create a dictionary with keys and their squares
print(squared_dict)

# 8. Checking Key Existence
print("name" in sample_dict)  # Returns True if key exists
print("age" in sample_dict)  # Returns False if key doesn't exist

# 9. Using Dictionaries with Default Values (defaultdict)
from collections import defaultdict

# Creating a defaultdict with default integer value
default_dict = defaultdict(int)
default_dict["apples"] += 1  # Incrementing the value even if key doesn't exist
print(default_dict)

# Creating a defaultdict with default list value
list_dict = defaultdict(list)
list_dict["fruits"].append("apple")
print(list_dict)

# 10. Merging Dictionaries (Python 3.9+)
dict1 = {"x": 10, "y": 20}
dict2 = {"y": 30, "z": 40}

# Merging using the | operator (Python 3.9+)
merged_dict = dict1 | dict2
print(merged_dict)

# Merging using the ** operator (older versions of Python)
merged_dict_old = {**dict1, **dict2}
print(merged_dict_old)

# 11. Dictionary as a Counter
from collections import Counter

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(fruits)
print(counter)  # Outputs the count of each element

# 12. Sorting a Dictionary by Keys and Values
# Sorting by keys
sorted_by_keys = dict(sorted(sample_dict.items()))
print(f"Sorted by keys: {sorted_by_keys}")

# Sorting by values
sorted_by_values = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print(f"Sorted by values: {sorted_by_values}")

# 13. Using frozenset as Dictionary Keys (Immutable Set)
frozenset_dict = {frozenset([1, 2, 3]): "Immutable set key"}
print(frozenset_dict)

# 14. Dictionary of Dictionaries (Nested Dictionaries)
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(nested_dict["person1"]["name"])  # Accessing nested dictionary values


# 15. Copying Dictionaries
original_dict = {"name": "John", "age": 25}

# Shallow copy using copy() method
shallow_copy = original_dict.copy()
print(f"Shallow copy: {shallow_copy}")

# Shallow copy using dict() constructor
shallow_copy_2 = dict(original_dict)
print(f"Shallow copy (dict constructor): {shallow_copy_2}")

# Deep copy of a nested dictionary
import copy
nested_dict = {"person": {"name": "Alice", "age": 30}}
deep_copy = copy.deepcopy(nested_dict)
print(f"Deep copy: {deep_copy}")

# 16. Dictionary from a List of Tuples
tuple_list = [("a", 1), ("b", 2), ("c", 3)]
dict_from_tuples = dict(tuple_list)
print(f"Dictionary from list of tuples: {dict_from_tuples}")

# 17. Inverting a Dictionary (Swapping Keys and Values)
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in original_dict.items()}
print(f"Inverted dictionary: {inverted_dict}")

# 18. Counting the Frequency of Elements in a List
# Manually count the frequency using a dictionary
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(f"Frequency count: {frequency}")

# Using collections.Counter (more efficient)
from collections import Counter
counter_frequency = Counter(data)
print(f"Frequency using Counter: {counter_frequency}")

# 19. Grouping Data by a Key
data = [
    {"name": "Alice", "department": "HR"},
    {"name": "Bob", "department": "IT"},
    {"name": "Charlie", "department": "HR"},
    {"name": "David", "department": "IT"}
]

# Group data by department
grouped_data = defaultdict(list)
for person in data:
    grouped_data[person["department"]].append(person["name"])
print(f"Grouped by department: {grouped_data}")

# 20. Initializing a Dictionary with Default Values
keys = ["a", "b", "c"]
default_value = 0
dict_with_defaults = dict.fromkeys(keys, default_value)
print(f"Dictionary with default values: {dict_with_defaults}")

# 21. ChainMap for Multiple Dictionaries (collections.ChainMap)
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
chain = ChainMap(dict1, dict2)
print(f"ChainMap: {chain}")
print(f"Value of 'b': {chain['b']}")  # Gets value from dict1 first

# 22. Dictionary with Conditional Logic (Dictionary Comprehension)
numbers = range(10)
even_odd_dict = {x: ("even" if x % 2 == 0 else "odd") for x in numbers}
print(f"Even/Odd Dictionary: {even_odd_dict}")

# 23. Removing Dictionary Items While Iterating
# Safely remove items from a dictionary while iterating
scores = {"John": 85, "Alice": 90, "Bob": 70, "Charlie": 65}

# Remove entries with scores below 80
scores_to_keep = {k: v for k, v in scores.items() if v >= 80}
print(f"Filtered scores: {scores_to_keep}")

# 24. Combining Two Dictionaries with Dictionary Comprehension
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print(f"Combined dictionary: {combined_dict}")

# 25. Sorting a Dictionary by Length of Keys or Values
# Sorting by key length
sorted_by_key_length = dict(sorted(original_dict.items(), key=lambda item: len(item[0])))
print(f"Sorted by key length: {sorted_by_key_length}")

# Sorting by value length (if values are strings)
string_values_dict = {"short": "tiny", "longer": "medium", "longest": "extended"}
sorted_by_value_length = dict(sorted(string_values_dict.items(), key=lambda item: len(item[1])))
print(f"Sorted by value length: {sorted_by_value_length}")

# 26. Find Minimum and Maximum Key/Value in a Dictionary
price_dict = {"apple": 5, "banana": 2, "orange": 3}

# Finding the minimum and maximum price
min_price = min(price_dict.items(), key=lambda x: x[1])
max_price = max(price_dict.items(), key=lambda x: x[1])
print(f"Minimum price: {min_price}")
print(f"Maximum price: {max_price}")

# 27. Working with JSON-like Data (Convert Dict to JSON and Vice Versa)
import json

# Convert dictionary to JSON string
data_dict = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(data_dict)
print(f"JSON string: {json_data}")

# Convert JSON string back to dictionary
parsed_dict = json.loads(json_data)
print(f"Parsed dictionary: {parsed_dict}")

# 28. Dictionary as Function Switch/Mapping (Function Pointers in Dictionaries)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "undefined"

# Function map using dictionary
operation_dict = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# Perform operations using the dictionary map
operation = "multiply"
result = operation_dict[operation](5, 3)
print(f"Result of {operation}: {result}")

# 29. Dictionary-Based Frequency Counter (Multiple Keys)
sentence = "This is a simple example of a dictionary-based frequency counter example"
word_list = sentence.lower().split()

# Frequency counter with multiple words
word_freq = defaultdict(int)
for word in word_list:
    word_freq[word] += 1
print(f"Word frequency: {word_freq}")

# 30. Dictionary and Enum Integration
from enum import Enum

class Status(Enum):
    SUCCESS = 1
    FAILURE = 0
    PENDING = 2

# Dictionary with Enum keys
status_dict = {
    Status.SUCCESS: "Operation was successful",
    Status.FAILURE: "Operation failed",
    Status.PENDING: "Operation is pending"
}
print(f"Status message: {status_dict[Status.SUCCESS]}")

