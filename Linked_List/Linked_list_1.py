#Node 구현

class Node :
    def __init__(self, value=0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
first.value = 6


#insert back or append

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node # 처음만 new node를 가리키게 한다.
        else:
            current = self.head
            while(current.next): # node의 마지막 까지 반복
                current = current.next
            current.next = new_node # 마지막 노드가 오면 다음 노드의 주솟값 가리킴
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value


#구현은 항상 문제 , 사람 , 상황에 따라 항상 바뀔 수 밖에 없다.

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

#get() 해당 위치에 리스트의 값을 리턴

#여기서 걸리는 것 파이썬 Class 사용법, self 인자

''''''