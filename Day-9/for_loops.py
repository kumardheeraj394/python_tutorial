# 'for', 'in', and 'range' are Python keywords, and 'i' is a variable
print("---use range----")
for i in range(10):  # use parentheses with range
    print(i)
   # print()

# 'for', 'in', and 'color' are Python keywords, and 'x' is a variable
print("---use list----")
color = ["red", "green", "yellow"] #color is list
for x in color:  # use parentheses with range
    print(x)  
    #print()  

# break
print("--- Use of break ---")
number = [1, 2, 3, 4, 5, 6]  # number is a list
for x in number:
    print(x)
    if x == 4:
        break  # exit the loop when x is 4 

# continue
print("--- Use of continue ---")
number = [1, 2, 3, 4, 5, 6]
for y in number:
    if y == 4:
        continue  # skip the print when y == 4
    print(y)
