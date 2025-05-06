# Program to append
print("=== Append Example ===")
list = ["a", "b", "c", "d"]
list.append("e")  # Add element to list
print("List after append:", list)
print("Type of list:", type(list))
print()

# Program to remove
print("=== Remove Example ===")
list = ["a", "b", "c", "d"]
list.remove("c")  # Remove element from list
print("List after remove:", list)
print("Type of list:", type(list))
print()

# Index
print("=== Index Access Example ===")
list = ["a", "b", "c", "d", "f"]
print("Element at index 1:", list[1])  # Accessing element by index
print()

# Length
print("=== Length of List ===")
list = ["a", "b", "c", "d", "f"]
print("Length of list:", len(list))
print()

# After append
print("=== Length After Append ===")
list = ["a", "b", "c", "d", "f"]
list.append("e") #
print("List after append:", list) #This prints the updated list
print("Length after append:", len(list)) #calculates and returns the number of items in the list.
print() #This simply prints a blank line for better readability of the output.

# After remove
print("=== Length After Remove ===")
list = ["a", "b", "c", "d", "f"]
list.remove("b")
print("List after remove:", list)
print("Length after remove:", len(list))

print("---Sort the number----")
number = [1, 20, 10, 5]
number.sort()
print("sorted number:",(number))

# concatinate
print("=== concatinate ===")
list = ["a", "b", "c", "d", "f"]
print("concatinate:",list[0]+"--"+(list[1]+"--"+(list[2])))  # showing 0index+1index
