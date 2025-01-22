

# palindrome
# -------------

test = input("enter any string:")
print("test_string: ", test)

rev_string = test[::-1]
print("reverse string: ", rev_string)

if test == rev_string:
    print("palindrome")
else:
    print("not a palindrome")