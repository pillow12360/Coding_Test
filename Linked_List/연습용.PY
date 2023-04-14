# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList():
#     def __init__(self,value):
#         self.head = None
#         self.tail = None


#     def append(self,value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next= new_node

#             self.tail = new_node

from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)

print(q)

q.pop()
print(q)

q.popleft()
print(q)


# class Node():
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#         self.prev = None

# class LinkedList(object):
#     def __init__(self,value):
#         self.head = None
#         self.tail = None
    
#     def append(self, value):
#       new_node = Node()

#       if self.head is None:
#           self.head = new_node
#           self.tail = new_node
#       else:
#           self.tail.next = new_node
#           new_node.prev = self.tail
#           self.tail = new_node

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self,value):
        self.head = None
        self.tail = None
    def append(self, value):
        new_node = Node()
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # self.tail.next = new_node
            # new_node.prev = self.tail
            # self.tail = new_node
            self.tail.next = new_node
            self.tail = self.tail.next

    def get():
        def __init__(self,idx):
            current = self.head
            for _ in range(idx):
                current = current.next
            return current.value
        
    def insert_at ():
        def __init__ (self,idx,value):
            current = self.head
            for _ in range(idx):
                currunt = current.next
            insert_node = Node()
            insert_node.value=value
            insert_node.next = current.next
            current.next = insert_node

    def remove(self,idx):
        current = self.head
        for _ in range(idx-1):
            current = current.next
            current.next = self.next


ll =LinkedList()
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)
ll.insert(idx=2, value=9)

