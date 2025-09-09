# Q3: 
# Given a pointer to the head node of a linked list, print each node's data element, one per 
# line. If the head pointer is null (indicating the list is empty), there is nothing to print. 
# Function Description 
# Complete the printLinkedList function in the editor below. 
# printLinkedList has the following parameter(s): 
# SinglyLinkedListNode head: a reference to the head of the list  
# Print For each node, print its data value on a new line 
# Returns 
# int[n]: the rotated array

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.display()

