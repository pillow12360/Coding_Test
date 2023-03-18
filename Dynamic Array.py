a = [1,2,3] # O(1)

a[0] # O(1)

a[1] = 9 # O(1)

a.append(4) # O(1)

a.append(5)

a.append(6) # O(1) Resizing

a.pop() #O(1)

a.insert(1,10) # O(n)

a.pop(2) #O(n)