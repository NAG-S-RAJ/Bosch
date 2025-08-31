# two strings are anagrams
a = input("Enter the first word")
b = input("Enter the second word")
a = list(a.lower())
b = list(b.lower())
a.sort()
b.sort()
if a == b:
    print("The given words form Anagrams")
else:
    print("The given words are not Anagrams")



'''
Another approach instead of converting to list and then sort there is functino called sorted() used to sort the strings and we can compare
sorted(a) ==sorted(b)
'''