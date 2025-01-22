import keyword

print(keyword.kwlist)

print(True)

print(keyword.iskeyword("True"))
print(keyword.iskeyword("true"))

#keywords are not identifiers, 
# starts with character(case-sensitive) a-z, A-Z, _
# remaining: A-Z, a-z, _, 0-9

name = 'anusha'
name_of_student = "Sravan"
student_math_01 = "poojitha"

#Constants
PI = 3.1425
DOZEN = 12
print(PI, DOZEN)

# built-in 
print("__name__=", __name__)
print("__file__=",__file__)