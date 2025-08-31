#common elements between list

a = [1,2,3,4,5,6]
b = [4,5,6,7,8,9]
print("Repeated Values: ")
for i in range(len(a)):
    if a[i] in b:
        print(a[i],end = " ")

''' other easy approach

c = set(a) & set(b)
print(c)

'''