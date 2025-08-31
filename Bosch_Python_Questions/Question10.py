# sort list without using sort()

a = [10,9,2,4,5,6,2,53]

for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j+1]<a[j]:
            a[j],a[j+1] = a[j+1],a[j]

print("Sorted List: ",a)