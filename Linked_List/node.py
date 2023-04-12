# Node 구현해보기

class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

# first = Node(1)
# second = Node(2)
# third = Node(3)

# first.next = second
# second.next = third
# first.value = 6

# append 오퍼레이션 구션

class LinkedList(object):
    def __init__(self): 
        self.head = None # 생성시 셀프를 None 값으로 초기화
    def append(self, value):
        new_node = Node(value) # 새 노드 생성
        if self.head is None: # 처음 생성시 에만 
            self.head = new_node #헤드가 첫번째 new_Node의 Node를 가리키게 함
        else: 
            current = self.head
            while(current.next): # current의 next 노드가 none이 될때까지 (마지막까지)
                current = current.next #current를 다음 커런트로 
            current.next = new_node 
            
# 이 코드는 항상 상황에 따라서 바뀔 수 있음 따라서 구동원리를 이해하고 활용할 수 있어야 함 

ll = LinkedList()

ll = append(1)
ll = append(2)
        