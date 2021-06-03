

#O(N)
# --> 스택은 미로 찾기, 트리의 순회, 그래프의 탐색 등을 수행하는데 기본이 되는 자료구조이다.

# 스택은 한 쪽 끝에서만 항목(item)을 삭제하거나 새로운 항목을 저장하는 자료구조이다.

def push(item):
    stack.append(item)

def peek():
    if len(stack) != 0:
        return stack[-1]

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item


stack = []
push('apple')
push('orange')
push('cherry')

print(stack)
pop()
print(stack)


