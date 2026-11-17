# There are two different things we can compare in Python:

# 1. Equality operator (==)

# Checks whether two objects contain equal values.
# • first_list == second_list -> True because both lists contain
#   [10, 20, 30].

# • first_list == third_list -> True because they also contain
#   identical values.

# 2. Identity operator (is)

# Checks whether two variables refer to the exact same object in memory.
# • first_list is second_list -> False because Python created two
#   separate list objects.

# • first_list is third_list -> True because third_list references
#   the same object as first_list.

# Create two separate lists with identical contents.
first_list = [10, 20, 30]
second_list = [10, 20, 30]

# Create a third variable referencing the first list.
third_list = first_list

# Compare the values of the lists.
print("first_list == second_list:", first_list == second_list)
print("first_list == third_list:", first_list == third_list)

# Compare the identities of the lists.

# Returns False because Python created two separate list objects
# in memory, even though they contain exactly the same values.
print("\nfirst_list is second_list:", first_list is second_list)

# Returns True because third_list references the exact same list
# object as first_list.
print("first_list is third_list:", first_list is third_list)