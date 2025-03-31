
Linked list 관련된 코드입니다. linkedlist를 파이썬으로 구현한 내용인데, 
class를 이용해서 구현하는 것을 알 수 있고, 그 클래스형을 이용한 여러 함수 __init__을 통해 다채로운 구현을 해나간다는게 큰 흐름이다.
class Node:
    def __init__(self,data, link = None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head =None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        current =  self.head
        while  current.link:
            current = current.link
        current.link = Node(data)

l1 = LinkedList()
l1.append(0)
l1.append(10)
l1.append(220)
print(l1)
