#fibonacci series upto n terms
n = int(input("Enter the input: "))
a= 0
b = 1
if(n == 0):
    print("No input given")
if (n ==1):
    print(0)
if (n >= 2):
    print(a,b,end=" ")
while(n-2>0):
    temp = b
    b = a+b
    a = temp
    print(b,end = " ")
    n-=1
    
