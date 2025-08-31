# count vowels and consonants in a string

vowels = ['a','e','i','o','u']
a = input("Enter the string")
a= a.lower()
a= a.replace(" ","")
counter = 0
n = len(a)
for i in range(0,n):
    if (a[i] in vowels):
        counter+=1

if (counter == 0):
    print("No inputs provided")
if (counter !=0):
    print("Total vowels count : ",counter)
    print("Total Consonant count : ",n-counter)
