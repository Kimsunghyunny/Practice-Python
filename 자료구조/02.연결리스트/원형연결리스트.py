

# O()
# --> 우선순위큐

#원형연결리스트는 마지막 노드가 첫 노드와 연결된 단순연결리스트이다.

#따라서 마지막 노드와 첫노드를 O(1)에 방문할 수 있는 장점이 있다.
#또한 empty가 아니면 어떤 노드도 None을 가지고 있지 않으므로 프로그램에서 None 조건 검사가 필요없어진다.


class CList:
    class _Node:
        def __init__ (self, item, link):
            self.item = item
            self.link = link
    
    def __init__ (self):
        self.last = None
        self.size = 0

    def no_items(self):
        return self.size
    
    def is_empty(self):
        return self.sizee == 0
    
    def insert(self, item):
        n = self._Node(item, None)
        if self.is_empty() :
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1
    
    def first(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        f = self.last.next 
        return f.item
    
    def delet(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -= 1
        return x.item
    
    def print_list(self):
        if self.is_empty():
            print("Empty")
        else:
            f = self.last.next 
            p = f
            while p.next != f:
                print(p.item, ' -> ', end='')
                p = p.next
            print(p.item)

class EmptyError(Exception):
    pass