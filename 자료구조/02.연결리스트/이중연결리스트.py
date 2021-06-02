

# O(N)
# --> 데크, 이항힙, 피보나치힙과 같은 우선순위큐 구현에 사용

#이중연결리스트는 각 노드가 두 개의 레퍼런스를 가지고 각각 이전 노드와 다음 노드를 가리키는 연결리스트.

class DList:
    class Node:
        def __init__ (self, item, prev, link):
            self.item = item
            self.prev = prev
            self.link = link
    
    #생성자
    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1
    
    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size -= 1
        return x.item
    
    def print_list(self):
        if self.is_empty():
            print("Empty")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):
    pass    