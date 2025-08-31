# count number of words in text file

f = open("write.txt","w")
a = input("Enter the text: ")
f.write(a)
f.close()

f1 = open("write.txt","r")
m = f1.read().split()
print("Total words in the File",len(m))
