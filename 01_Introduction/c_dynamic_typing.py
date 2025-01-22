

num1=100
type(num1)

print(type(num1))
print("num1", num1)
print("num1 = ", num1)

# works in both static and dynamic typing
num1=300
print("num1=", num1, "type=", type(num1))

# python is a dynamic typed language
num1 = 300.0
print("num1=", num1, "type=", type(num1))

num1 = 300.
print("num1=", num1, "type=", type(num1))

num1 = 300,
print("num1=", num1, "type=", type(num1))

num1 = (300,)
print("num1=", num1, "type=", type(num1))

num1 = -0.09
print("num1=", num1, "type=", type(num1))

num1 = -0.09j
print("num1=", num1, "type=", type(num1))

num1 = "300"
print("num1=", num1, "type=", type(num1))

num1 = True
print("num1=", num1, "type=", type(num1))

num1 = None
print("num1=", num1, "type=", type(num1))
