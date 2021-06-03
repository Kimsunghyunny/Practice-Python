

#O(N)
# --> 스택과 큐, 해싱의 체이닝, 트리와 연관 (+ 비트코인 블록체인도 단순연결리스트 응용)

#단순연결리스트는 동적 메모리 할당을 이용해 노드들을 한 방향으로 연결하여 리스트를 구현하는 자료구조


#단순연결리스트는 삽입이나 삭제시에 항목들의 이동이 필요없다.
#반면 항목 탐색을 위해서는 항상 첫 노드부터 원하는 노드를 찾을때 까지 차례로 방문하는 순차탐색을 해야한다.


class SList:
    class Node:
        def __init__(self, item, link): 
            self.item = item
            self.next = link
        
        #생성자
    def __init__(self):
            self.head = None
            self.size = 0
        
        #
    def size(self):
            return self.size
        
    def is_empty(self):
            return self.siez ==0
        
    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None) # head에 item값 넣고 이어지는게 없으니 link는 none으로 저장
        else:
            self.head = self.Node(item, self.head) # head가 있음에도 새로운 값을 넣으려 할때
        self.size += 1
        
    def insert_after(self,item, p): # p가 가리키는 노드에 다음에 새 노드를 삽입한다.
        p.next = SList.Node(item, p.next) # 새 노드가 p의 다음 노드가 되어 연결된다.
        self.size += 1
        
    def delete_front(self):
        if self.is_empty():
            raise EmpytyError('Underflow')
        else:
            self.head = self.head.next
        self.size -= 1
        
    def delete_after(self, p): # p가 가리키는 노드의 다음 노드를 삭제한다.
        if self.is_empty():
            raise EmptyError('Underfolw')
        t = p.next
        p.next = t.next
        self.size -= 1
        
    def search(self,target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next 
        return None
        
    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass