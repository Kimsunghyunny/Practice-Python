"""
파이썬에서 리스트들은 일렬로 저장하기 때문에 연산이 순차적으로 수행되어야한다는 단점이 있다.
파이썬의 리스트는 미리 정렬해 놓으면 이진 탐색을 통해 효율적인 탐색이 가능하지만, 삽입이나 삭제 후에도 정렬 상태를 유지해야 하므로
삽입이나 삭제하는데 o(n)의 시간이 소요된다.
트리는, 이러한 문제점을 보완한 계층적 자료구조이다.

--> 트리는 일반적인 트리, 이진트리로 구분되며
    이진 트리에서는 다양한 탐색트리, 힙 등의 자료구조로서 응용된다.


이진힙은 우선순위 큐를 구현하는 가장 기본적인 자료구조이다. 
우선순위큐란 가장 높은 우선순위를 가진 항목에 접근하거나 해당 항목을 삭제하는 연산과 임의의 우선순위를 가진 항목을 삽입하는 연산을 지원하는 자료구조이다.
우선순위큐는 스택과 큐로도 구현할 수 있는데, 왜 또 다른 우선순위 큐가 필요할까?
--> 스택은, 새로이 저장되는 항목의 우선순위는 기존에 저장되어 있던 모든 항목보다 우선순위가 더 놓고,
    큐는, 새롭게 삽입되는 항목의 우선순위는 큐에 기존에 저장되어 있던 모든 항목들의 우선순위보다 낮다.
    그러나 일반적으로 새롭게 삽입되는 항목이 임의의 우선순위를 가진다면 스택이나 큐는 새 항목이 삽입될 때마다 항목들을 우선순위에 따라 정렬하는 상태를 유지해야하는 문제가 발생한다.
    따라서 이러한 문제를 해결하기 위해서 새 항목 삽입 시 정렬된 상태를 유지할 필요가 없고, o(1) 시간에 가장 높은 우선순위 항목에 접근할 수 있으며
    가장 높은 우선순위를 가진 항목을 삭제하는 연산을 지원하는 자료구조는 이진힙이다.


* 이진힙
이진힙은 완전이진트리로서 부모의 우선순위가 자식의 우선순위보다 높은 자료구조이다.
(완전이진트리는 마지막 레벨을 제외한 각 레벨이 노드들로 꽉 차있고, 마지막 레벨에는 노드들이 왼쪽부터 빠짐없이 채워진 트리)

* 이진힙의 종류 - 최소힙, 최대힙
1) 최소힙 : 키 값이 작을수록 높은 우선순위를 가지는 힙
2) 최대힙 : 키 값이 클수록 더 높은 우선순위를 가지는 힙

"""

# 여기에서는 최소 이진힙을 구현한다.


class BHeap:
    def __init__(self, a): # 리스트 a, 항목수 N
        self.a = a
        self.N = len(a)-1

    def create_heap(self):
        for i in range(self.N/2, 0, -1):
            self.downheap(i)
    
    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_min(self):
        if self.N == 0:
            print('힙이 비어 있음')
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1
        self.downheap(1)
        return minimum
    
    def downheap(self, i):
        while 2*i <= self.N:
            k = 2*i
            if k <self.N and self.a[k][0] > self.a[k+1][0]:
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = k

    def upheap(self, j):
        while j > 1 and self.a[j//2][0] > self.a[j][0]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j//2

    def print_heap(self):
        for i in range(1, slef.N+1):
            print('[%2d' % self.a[i][0], self.a[i][1], ']', end='')
        print('\n힙 크기 = ', self.N)