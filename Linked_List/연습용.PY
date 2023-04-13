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


class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self,value):
        self.head = None
        self.tail = None
    
    def append(self, value):
      new_node = Node()

      if self.head is None:
          self.head = new_node
          self.tail = new_node
      else:
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node
              
