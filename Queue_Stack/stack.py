# stack

# 큐는 단독사용 거의 없고 다른 알고리즘, 구현할 때 같이 사용

# 스택은 스택자체로 코테에서 많이 나온다. 단독으로 많이 쓰이므로 중요한 자료구조 중 하나이다. 

# stack은 array리스트도 빅오 1이므로 링크드 리스트를 사용할 필요가 없다. 리스트사용방법과 같다.

#자연스레 이해하고 넘어가도 된다.

stack = []

stack.append(1)
stack.append(2)
stack.append(2)

stack.pop()
stack.pop()
stack.pop()

# LIFO