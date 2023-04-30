# 리스트를 사용하여 큐 구현

q = []

q.append(1)
q.append(2)
q.append(3)

q.pop(0)
q.pop(0)

# Linked list 기반 구현

# 맨앞
# appendleft()
# popleft()

# 맨뒤
# append()
# pop()


# list based queue

# 링크드 리스트 베이스 큐 구현

from collections import deque

queue = deque()

queue.append(1) # O(1)
queue.append(2)
queue.append(3)

queue.popleft() # O(1)
queue.popleft()
queue.popleft()

# 파이썬에서 이미 dequeue를 링크드리스트 베이스로 구현해놓음 따라서 시간 복잡도가 O(1)인 dequeue를 바로 사용가능

#front rear 가 있다.

# 양방향으로 디큐 , 인큐가 가능한다.

# doubly
# ended
# que queue

# 디큐, 인큐를 빅오 1으로 계산가능한 것 기억
# 큐는 다른 알고리즘과 같이 쓰인다.