# second largest number in list
a = [1,2,3,4,5,6,7,8]
a1 = a.copy()

max_value = max(a1)
a1.remove(max_value)
print("Second Greatest Number: ",max(a1))
print(a)
print(a1)