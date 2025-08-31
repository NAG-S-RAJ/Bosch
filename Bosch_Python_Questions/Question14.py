# accept kwargs and return sum of values

def add(**kwargs):
    return sum(kwargs.values())

a = add(a = 10,b=20,c=30)
print("Sum of the values: ",a)