#Linked List 연습
\
class Node :
    def __init__(self, value=0, next = None):
            self.value = value
            self.next = next


class Linkedlist(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
             current = self.head
             while(current.next):
                  