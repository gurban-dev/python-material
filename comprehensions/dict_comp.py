# Dictionary comprehensions are used to create dictionaries in
# a concise way.

# Syntax:
# {key: value for (key, value) in iterable if condition}

# key: The item to use as the dictionary key.
# value: The item to use as a the dictionary value.
# iterable: Any sequence or collection to loop/iterate through.
# condition (optional): Lets you include only certain items.

# A condition is something that must be true for an event to occur.

# range(2, 11, 2) is the range: 2, 4, 6, 8, 10
squared_items = {i: i**2 for i in range(2, 11, 2)}

# squared_items = {
#     2: 4,
#     4: 16,
#     6: 36,
#     8: 64,
#     10: 100
# }

print(f"squared_items: {squared_items}")