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

# from collections import deque

# q = deque()

# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# q.append(6)

# print(q)

# q.pop()
# print(q)

# q.popleft()
# print(q)


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

# 0414

# class Node():
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#         self.prev = None

# class LinkedList():
#     def __init__(self,value):
#         self.head = None
#         self.tail = None
#     def append(self, value):
#         new_node = Node()
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # self.tail.next = new_node
#             # new_node.prev = self.tail
#             # self.tail = new_node
#             self.tail.next = new_node
#             self.tail = self.tail.next

#     def get():
#         def __init__(self,idx):
#             current = self.head
#             for _ in range(idx):
#                 current = current.next
#             return current.value
        
#     def insert():
#         def __init__ (self,idx,value):
#             current = self.head
#             for _ in range(idx):
#                 currunt = current.next
#             insert_node = Node()
#             insert_node.value=value
#             insert_node.next = current.next
#             current.next = insert_node

#     def remove(self,idx):
#         current = self.head
#         for _ in range(idx-1):
#             current = current.next
#             current.next = self.next

#     def print(self):
#         current = self.head
#         while (current):
#             print (current.value, end="")
#             current = current.nexti
#             if current:
#                 print("->",end=' ')
#         print()




# ll = LinkedList()
# ll.append(1)
# ll.append(1)
# ll.append(1)
# ll.append(1)
# ll.insert(idx=2, value=9)
# ll.print()


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# class LinkedList():
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def append (self,value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             self.value = value
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node

#     def get(self, idx):
#         current = self.head
#         for _ in range(idx):
#             current = current.next
#         return current.value

#     def insert(self,idx,value):
#         current = self.head
#         for _ in range(idx-1):
#             current = current.next
#         new_node = Node(value)
#         new_node.next = current.next
#         current.next = new_node
#         new_node.prev = current
        
#     def remove(self, idx):
#         if idx == 0:
#             self.head = self.head.next # garbage collector가 알아서 처리해준다.
#         else:
#             current = self.head
#             for _ in range(idx-1):
#                 current = current.next
#             current.next = current.next.next
    
#     def print(self):
#         current = self.head
#         while(current):
#             print(current.value, end="")
#             current = current.next    
#             if current:
#                 print("->", end="")
#         print()


# ll = LinkedList()

# ll.append(1)
# ll.append(10)
# ll.append(100)
# ll.append(1000)
# ll.append(10000)


# ll.print()

# ll.remove(5)

# ll.print()


class Node():
    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory():
    def __init__(self,homepage):
        self.head = self.current = Node(val=homepage)

    def visit(self,url):
        self.current.next = Node(val=url,prev=self.current)
        self.current = self.current.next
        return None
        
    def back(self,steps):
        while steps > 0 and self.current.prev != None:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
    
    def forward(self,steps):
        while steps > 0 and self.current.next != None:
            self.current = self.current.next
            steps -= 1
        return self.current.val

