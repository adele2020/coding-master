####################################################
# p.243
# 연결 리스트를 이용한 스택 ADT 구현
####################################################
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next= next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)
        print("{} = [ {} | {} ]".format(id(self.last), self.last.item, id(self.last.next)))

    def pop(self):
        item = self.last.item
        print("변경전 : {} = [ {} | {} ]".format(id(self.last), self.last.item, id(self.last.next)))
        self.last = self.last.next
        print("변경후 : {} = [ {} | {} ]".format(id(self.last), self.last.item, id(self.last.next)))

        return item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.pop()

for _ in range(5):
    print(stack.pop())


#print("{} = [ {} | {} ]".format(id(self.last), self.last.item, id(self.last.next)))
        #print("변경전 : {} = [ {} | {} ]".format(id(self.last), self.last.item, id(self.last.next)))
                #print("변경후 : {} = [ {} | {} ]".format(id(self.last), self.last.item, id(self.last.next)))
#################################################################################
#  자료형 deque의 내장 메서드를 사용하여 구현 (double-ended queue) 데이터 양방향으로 추거 제거
# O(1)의 시간 복잡도로 리스트보다 성능 상에 이점
################################################################################
from collections import deque

queue = deque([4, 5, 6])
queue.append(7)
queue.append(8)
queue

queue.popleft()
queue.popleft()
queue

#######################################################################
# 자료형 queue의 내장 메서드를 사용하여 구현
#######################################################################
import queue

q = queue.Queue()

q.put("a")
q.put("b")
q.put("c")

q.qsize()    # 3
q.get()      # 'a'
q.qsize()    # 2

#######################################################################
# 자료형 LifoQueue의 내장 메서드를 사용하여 구현
# Last in First Out Queue 구현하기
#######################################################################
import queue

q= queue.LifoQueue()
q.put("a")
q.put("b")

q.qsize()   #  2
q.get()     # 'b'

#######################################################################
# 자료형 PriorityQueue의 내장 메서드를 사용하여 구현
# 우선순위가 높은 큐가 먼저 나온다.
#######################################################################
import queue

q = queue.PriorityQueue()
q.put((10, "a"))
q.put((5, "b"))
q.put((15, "c"))
q.qsize()    # 3
q.get()      # (5, 'b')


#######################################################################
# 23. 큐를 이용한 스택 구현 (리트코드225.) *
# 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
# push(x): 요소 x를 스택에 삽입한다.
# pop(): 스택의 첫번째 요소를 삭제한다.
# top(): 스택의 첫 번째 요소를 가져온다.
# empty(): 스택이 비어 있는지 여부를 리턴한다.
#######################################################################
import collections
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft() #int

    def top(self):
        return self.q[0] #int

    def empty(self):
        return len(self.q) == 0 #bool

stack = MyStack()

stack.push(1)
stack.push(2)
stack.top()
stack.pop()
stack.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


def remove(s: str):
    for char in sorted(set(s)):
        suffix = s[s.index(char)]
        if set(s) == set(suffix)
            return char + self.remove(suffix.replace(char,''))
    return



print(set('cbacdcbc'))
