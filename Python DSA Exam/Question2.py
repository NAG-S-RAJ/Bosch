# Q2:  
# A left rotation operation on an array of size n shifts each of the array's elements 1 unit to 
# the left. Given an integer, d, rotate the array that many steps left and return the result. 
# Example 
# d=2 
# arr=[1,2,3,4,5] 
# After 2 rotations,
# arr’=[3,4,5,1,2] . 
# Function Description 
# Complete the rotateLeft function in the editor below. 
# rotateLeft has the following parameters: 
# int d: the amount to rotate by 
# int arr[n]: the array to rotate

lst = list(map(int,input("Enter the List data :").split()))
print(lst)
d = int(input("Key :"))
d = d%len(lst)
for i in range(d):
    temp = lst[0]
    lst.pop(0)
    lst.append(temp)

print(lst)