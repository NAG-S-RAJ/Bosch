# Q1:    
# A  sequence of brackets is balanced if the following conditions are met: 
# It contains no unmatched brackets. The subset of brackets enclosed within the confines of a 
# matched pair of brackets is also a matched pair of brackets. Given  n strings of brackets, 
# determine whether each sequence of brackets is balanced. If a string is balanced, return YES. 
# Otherwise, return NO. 
# Function Description 
# Complete the function isBalanced . 
# isBalanced has the following parameter(s): 
# string s: a string of brackets 
# Returns 
# string: either YES or NO

def Brackets(lt):
    dic = {'}':'{',')':'(',']':'['}
    stack = []
    for char in lt:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if not stack or stack.pop()!= dic[char]:
                return False
    return not stack
 
 
 
 
lt = input("Enter the brackets to check")
result =  Brackets(lt)
if result:
    print("YES")
else:
    print("NO")