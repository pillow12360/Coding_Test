class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, value):
        self.head = None
        self.value = value
        self.tail = None

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.haed = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # tail 다음 새 노드를 추가해주면 됨
            self.tail = new_node # tail 업데이트 
            
    def get(self, idx):
      current = self.head
      for _ in range(idx):
          current = current.next
      return current.value
    
    def intert(self,idx,value):
        current = self.head
        for _ in range(idx):
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        new_node.value = value
        current.va