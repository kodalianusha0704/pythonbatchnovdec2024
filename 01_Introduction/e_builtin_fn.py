

name = "bruno"
print(name)

print("name is: "+ name)
print("name is: ", name)
print("name is: ", name, sep='-')

print("name is: ", name, sep='-')
print(1,2,3,4,5,6, name, sep='~')

p = 120
 #print("value is: "+ p)  # TypeError: can only concatenate str (not "int") to str

print("value is: "+ str(p))

print("value is: "+ " "+ str(p))
