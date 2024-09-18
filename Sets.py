# sets.py

"""
Sets in Python

A set is an unordered collection of unique elements. Sets are mutable, meaning you can add and remove elements, but they do not allow duplicate items. They are useful for membership testing, eliminating duplicate entries, and performing set operations such as union, intersection, and difference.

1. Creation:
   - Sets can be created using curly braces `{}` or the `set()` function.

2. Adding Elements:
   - Use the `add()` method to add a single element.
   - Use the `update()` method to add multiple elements from an iterable.

3. Removing Elements:
   - Use the `remove()` method to remove a specific element. Raises a KeyError if the element is not present.
   - Use the `discard()` method to remove an element if present. Does not raise an error if the element is not found.
   - Use the `pop()` method to remove and return an arbitrary element.

4. Set Operations:
   - Union: `set1 | set2` or `set1.union(set2)`
   - Intersection: `set1 & set2` or `set1.intersection(set2)`
   - Difference: `set1 - set2` or `set1.difference(set2)`
   - Symmetric Difference: `set1 ^ set2` or `set1.symmetric_difference(set2)`

5. Set Methods:
   - `copy()`: Returns a shallow copy of the set.
   - `clear()`: Removes all elements from the set.
   - `len()`: Returns the number of elements in the set.
   - `in`: Tests membership.

Syntax:
# Creating a set
my_set = {1, 2, 3}

# Adding elements
my_set.add(4)
my_set.update([5, 6])

# Removing elements
my_set.remove(4)
my_set.discard(7)
my_set.pop()

# Set operations
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_diff_set = set1 ^ set2
"""

# Example 1: Creating and Adding Elements to a Set
my_set = {1, 2, 3}
print("Initial set:", my_set)

my_set.add(4)
print("After adding 4:", my_set)

my_set.update([5, 6])
print("After updating with [5, 6]:", my_set)

# Example 2: Removing Elements from a Set
my_set.remove(6)
print("After removing 6:", my_set)

my_set.discard(10)  # No error if 10 is not present
print("After discarding 10:", my_set)

# Example 3: Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2
print("Union:", union_set)

intersection_set = set1 & set2
print("Intersection:", intersection_set)

difference_set = set1 - set2
print("Difference:", difference_set)

symmetric_diff_set = set1 ^ set2
print("Symmetric Difference:", symmetric_diff_set)

# Example 4: Using Set Methods
copy_set = my_set.copy()
print("Copied set:", copy_set)

my_set.clear()
print("After clearing:", my_set)

# Example 5: Membership Testing
test_set = {1, 2, 3}
print("Is 2 in test_set?", 2 in test_set)
print("Is 4 in test_set?", 4 in test_set)

"""
Assignments

1. **Assignment 1**: Create a set with elements `1, 2, 3, 4, 5`. Add elements `6` and `7` to the set. Print the updated set.

2. **Assignment 2**: Create two sets, `set_a` with elements `1, 2, 3` and `set_b` with elements `3, 4, 5`. Perform and print the union, intersection, and difference of these sets.

3. **Assignment 3**: Write a program that removes an element from a set. If the element does not exist, discard it without raising an error. Print the final set.

4. **Assignment 4**: Create a set and test if a specific element is present in it. Print a message indicating whether the element is found or not.

5. **Assignment 5**: Write a function that accepts two sets and returns their symmetric difference. Test the function with sample sets and print the result.

"""

# Solved Assignments

# Solved Assignment 1
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

my_set.add(6)
my_set.add(7)
print("After adding 6 and 7:", my_set)

# Solved Assignment 2
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
print("Union:", union_set)

intersection_set = set_a & set_b
print("Intersection:", intersection_set)

difference_set = set_a - set_b
print("Difference:", difference_set)

# Solved Assignment 3
my_set = {1, 2, 3, 4}
print("Original set:", my_set)

my_set.remove(3)  # Raises KeyError if 3 is not present, use discard() to avoid error
print("After removing 3:", my_set)

my_set.discard(5)  # No error if 5 is not present
print("After discarding 5:", my_set)

# Solved Assignment 4
test_set = {1, 2, 3}
element = 2
print(f"Is {element} in test_set? {'Yes' if element in test_set else 'No'}")

element = 4
print(f"Is {element} in test_set? {'Yes' if element in test_set else 'No'}")

# Solved Assignment 5
def symmetric_difference(set1, set2):
    return set1 ^ set2

set_x = {1, 2, 3}
set_y = {2, 3, 4}
result = symmetric_difference(set_x, set_y)
print("Symmetric Difference:", result)
