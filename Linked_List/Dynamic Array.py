#Python의 List는 기본적으로 Dynamic Array로 구성되어 있다 따라서
#따로 구현하지 않고도 손쉽게 사용할 수 있다. 리스트 사용시 사이즈 선언이 필요 없는 장점
#아래 내용은 계산에 따라서 달라지는 시간복잡도를 빅-오 방식으로 표기하였다.


a = [1,2,3] # O(1)

a[0] # O(1)

a[1] = 9 # O(1)

a.append(4) # O(1)

a.append(5)

a.append(6) # O(1) Resizing

a.pop() #O(1)

a.insert(1,10) # O(n)

a.pop(2) #O(n)