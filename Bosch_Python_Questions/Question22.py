#Bubble sorting
a =[1,4,7,3,5,8,3,234]
n = len(a)
for i in range(n):
    for j in range(n-i-1):
        if (a[j+1]<a[j]):
            a[j],a[j+1] = a[j+1],a[j]
print("Sorted Array: ",a)