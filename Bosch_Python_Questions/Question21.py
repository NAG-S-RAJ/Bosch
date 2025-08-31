# Binary search

a = [10,23,42,45,2,15,6,3]
n = int(input("Enter the number: "))
a.sort()
print("Sorted Array: ",a)
l=0
r = len(a)-1
while(l<=r):
    if(n not in a):
        print("Please enter the correct input")
        break
    mid = int((l+r)/2)
    if(a[mid] == n):
        print(f"The value {n} is placed in {mid+1} position")
        break
    if(a[mid]<=n):
        l = mid+1
    if(a[mid]>n):
        r = mid-1
