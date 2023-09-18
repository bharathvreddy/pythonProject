class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head = node1
node1.next = node2

node2.next = node3
node3.next = node4

temp = head
while temp != None:
    print(temp.value)
    temp = temp.next