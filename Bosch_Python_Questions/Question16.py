# all prime numbers in a given range

n = int(input("Enter the range: "))
print("Prime Numbers are: ")
for i in range(2,n+1):
    is_prime = True
    for j in range(2,int(i**0.5)+1):
        if(i%j ==0):
            is_prime = False
            break
    if is_prime:
        print(i,end=" ")
