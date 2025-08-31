# Function to check if a number is even or odd

def addEven(num):
    if num%2 ==0:
        print("It is an Even number")
    else:
        print("It is an Odd number")

a = int(input("Enter only number: "))
addEven(a)