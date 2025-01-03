class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

#printing the linked list
# current = node1
# while current is not None:
#     print(current.data,end="->")
#     current = current.next

#Inserting a new element in the firstplace
head = node1
new_node = Node(50)
new_node.next = head
head = new_node

#Adding a new element to the last position
head = node1
current = head
new_node = Node(50)
while current.next is not None:
    current = current.next
current.next = new_node

