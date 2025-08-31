# Program to find the factorial of a number

a = int(input("Enter the number:"))

def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return a*fact(a-1)
    
print(f"The factorial of {a} is {fact(a)}")