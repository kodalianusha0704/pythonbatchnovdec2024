
"""
\t
\b
\n
r''
"""

print("hello world")
print("hello \tworld")
print("hello \nworld")
print("hello \bworld") #overwrites previous char


print("hello \nworld  \\nvijayawada")
print(r"hello \nworld \tpython")

#-------------------------
print("hello") #default end='\n'
print("world")

print("hello",end=" ")
print("world",end='\n')

print("hello",end="_____")
print("world",end='\n')

print("hello", "python", 123, end='\t')
print("hello", "python", 123, end='\n',sep=';')