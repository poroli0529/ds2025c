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
