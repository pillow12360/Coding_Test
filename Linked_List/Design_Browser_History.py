#인터넷 브라우저에서 방문기록과 동일한 작동을 하는 browser histroy class를 구현

#구현할 브라우저는 homepage에서 시작하고, 이후에는 url에 방문할 수 있다. 뒤로가기와 앞으로가기를 구현하라

# class Node():
#     def __init__(self,value: str):
#         self.value = value
#         self.next = None
#         self.prev = None

# class BrowserHistory():

#     def __init__(self, homepage: str):
#         self.homepage = homepage
#         self.head = None
#         self.tail = None

#     def visit(self, url: str) -> None:
#       new_page = Node(url)
#       if self.head is None:
#         self.head = new_page
#         self.tail = new_page
#         self.prev = new_page
#       else:
#         new_page.prev = self.tail
#         self.tail.next = new_page
#         self.tail = new_page

#     def print(self) -> None:
#       current = self.head
#       while(current):
#         print(current.value,end=" ")
#         current = current.next
        

#     def back(self, steps: int) -> str:
#         current = self.tail
#         for _ in range(steps):
#            current = current.prev
#         return current.value
        

#     def forward(self, steps: int) -> str:
#         pass
      
# browserHistory =BrowserHistory("aa.com")
# browserHistory.visit("abc1.com")
# browserHistory.visit("abc2.com")
# browserHistory.visit("abc3.com")
# browserHistory.visit("abc4.com")
# browserHistory.visit("abc5.com")

# browserHistory.visit("abc6.com")

# browserHistory.visit("abc7.com")

# browserHistory.print()
# print()
# print(browserHistory.back(4))

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

class ListNode(object):
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory():
    def __init__(self, homepage):
        self.head=self.current = ListNode(val=homepage)

    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        return None
    
    def back (self, steps):
        while steps > 0 and self.current.prev != None:
            steps -=1
            self.current = self.current.prev
        return self.current.val
    
    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val