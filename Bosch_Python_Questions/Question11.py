#count the frequency of each element in list

a = [10,9,2,4,5,6,2,53,10,9,4,4,4,6]
dict1 = {}
for i in range(len(a)):
    if a[i] in dict1.keys():
        dict1[a[i]]+=1
    if a[i] not in dict1.keys():
        dict1[a[i]] = 1
    
    
print("Values","|","Frequencies")
for key,value in dict1.items():
    print(key,"|",value)
