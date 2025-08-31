# function to reverse a string

a = input("Enter the String: ")

for i in range(-1,-(len(a)+1),-1):
    print(a[i],end="")

"""
a1 = a[::-1]
print(a1)     It will print the reverse of the string
"""
