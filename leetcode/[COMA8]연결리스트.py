#######################################################################
# 15. 역순연결리스 (리트코드206.) *
# 연결리스트를 뒤집어라
# input = 1->2->3->4->5->NULL
# output = 5->4->3->2->1->NULL
#######################################################################
"""
1|2 -- 2|3 -- 3|4 -- 4|5 -- 5|None
5|4 -- 4|3 -- 3|2 -- 2|1 -- 1|None

아래 코드 순서대로 실행해보기
"""
################################ 입력값만들기
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

############################### 입력값 확인 : 연결리스트기 때문에 반복문을 사용해야 함
node = node1
################ ID값으로 보기
while node:
    print("{} : {} | {}".format(node.val,id(node),id(node.next)))
    node = node.next
################ 객체 자체로 보기 (안봐도 됨.봐도 되고..)
while node:
    print("{} : {} | {}".format(node.val,node,node.next))
    node = node.next


###################################문제해결함수
def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev
############################## 함수 실행
reverseList(node1) #node1이 처음 연결 객체니까..

"""
node : 1|2
prev : None
--------------------------------1 - 1|2
118줄
next : 2가 가리키는 2|3
node.next : None

119줄
prev : 1|None
node : 2가 가리키는 2|3
------------------------------2 - 2|3
118
next : 3이 가리키는 3|4
node.next : 1|None

119
prev : 2|1
node : 3이 가리키는 3|4
"""

############################### 결과값 확인 : 연결리스트기 때문에 반복문을 사용해야 함
node = node5 #reverse 되면 node5가 처음 값이 되니까...
################ ID값으로 보기
while node:
    print("{} : {} | {}".format(node.val,id(node),id(node.next)))
    node = node.next
