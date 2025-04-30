#Create two boolean variables, x and y.
#Use logical operators (and, or, not) to perform various logical operations on x and y.
#Print the results.
a = 3
b = 2
x = a is b #true

c = 5
d = 2
y = c is d #false

and_r = x and y
or_r = x or y
not_result_x = not x
not_result_y = not y

# Use logical operators (and, or, not) to perform logical operations
print("and operation:", and_r)     # True and True -> True
print("or operation:", or_r)       # True or True -> True
print("not x:", not_result_x)
print("not y:", not_result_y)
