class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.value = value
        else:
            self.tail.next = new_node
            self.tail.prev = self.tail
            self.tail = new_node

    def get (self,idx):
        self.current = self.head
        for _ in range(idx):
            self.current = self.current.next
        return self.current.value
    
    def remove (self, idx):
        None





ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print(ll.get(2))

