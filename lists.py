# Lists are mutable - items can be changed within the list, essentially replaced

# Example list [1, 9, 8]

a = ["apple", "orange", "pear"]
a[1]
print(a[0])

# replace orange in position 1 with the number 7

a[1] = 7
print(a)

# append items into an empty list 
# b variable has a value of an empty list - use the append method to add the integer to the list

b = []
b.append(1)
print(b)