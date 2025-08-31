a = input("Enter the sentence: ")
a = a.split()
max_length = max(a,key = len)

print(f"Longest word is {max_length}")