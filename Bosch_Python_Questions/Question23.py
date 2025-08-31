# Rotate a list by k position
a = [1,2,3,4,5]
n = int(input("Enter how many position to rotate"))
for i in range(n):
    l = a[i]
    a.pop(0)
    a.append(l)

print("Rotated Array: ", a)
