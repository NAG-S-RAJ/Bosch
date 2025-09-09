# Q6: 
# Given the pointer to the head node of a linked list, change the next pointers of the nodes so 
# that their order is reversed. The head pointer given may be null meaning that the initial list is 
# empty. 
 
# Example 
# head references the list 1→2→3→NULL 
# Manipulate the next pointers of each node in place and return head, now referencing the 
# head of the list 3→2→1→ NULL. 
# Function Description 
# Complete the reverse function in the editor below. 
# reverse has the following parameter: 
# • SinglyLinkedListNode pointer head: a reference to the head of a list 
# Returns 
# • SinglyLinkedListNode pointer: a reference to the head of the reversed list 

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next    
        current.next = prev         
        prev = current              
        current = next_node         
        
    return prev  

head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)

new_head = reverse(head)

curr = new_head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")
