# string is palindrome or not
a = input("Enter the string: ")
a = a.lower()
a1 = a[::-1]
if (a1 == a):
    print("It is palindrome")
else:
    print("It is not a palindrome")