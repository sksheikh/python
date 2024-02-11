# variable
# x = 5 # int type
# y = "Sheikh Salah Uddin" # str type

# print(x)
# print(y)

# casting
# x = str(3) # x == '3
# y = int(3) # y == 3
# z = float(3) # z == 3.0
# print(type(x))
# print(type(y))
# print(type(z))

# firstName = 'Sheikh' # allowed
# 2firstName = 'Sheikh' # not allowed

# lastName = 'Salah Uddin' #camel case
# LastName = 'Salah Uddin' #pascel case
# last_name = 'Salah Uddin' #snake case


# many values to multiple variables
# x, y, z = "orange", "Banana", "Cherry"

# one value to multiple variables
# x = y = z = "Apple"

# unpacking a collection
# fruits = ["apple", "orange", "banana"]
# x, y, z = fruits
# print(fruits)

# x = "Python "
# y = "is "
# z = "awesome"

# x = 5;
# y = 10;
# print(x + y)
# print(y)
# print(z)

x = "Python"

def myFunc():
  global x
  x = "JavaScript"
  print("I Love " + x)

myFunc()

print("I Love " + x)
