
# ----------------------------------------------------------------------------------------------------
# 1. 컬렉션 관리 함수
# 컬렉션은 여러 개의 값을 저장한다는 면에서 기능적으로 비슷해 관리하는 방법도 유사하다.


# 1) enumerate
# 순서값과 요소값을 한꺼번에 구해주는 내장함수

score = [88, 95, 70, 100, 99]
for no, s in enumerate(score,1): # 1부터 시작하는 순서값과 요소값을 튜플로 생성 즉, (1,88), (2,95), (3,70).. 으로 튜플 생성
    print(str(no) + '번 학생의 성적:', s)


# 2) zip
# zip 함수는 여러 개의 컬렉션을 하나로 만든다.

yoil = ['월', '화', '수', '목', '금', '토','일']
food = ['갈비탕', '순대국', '칼국수', '삼겹살']
menu = zip(yoil, food)
for y, f in menu:
    print('%s요일 메뉴:%s' %(y,f))
# 길이가 짧은 food에 맞춰서 4개의 요소끼리 합쳐 튜플로 생성된다.


# ----------------------------------------------------------------------------------------------------

# 2. 람다함수

# 1) filter
# filter 함수는 리스트의 요소 중 조건에 맞는 것만 골라낸다.
# 첫번쨰 인수는 조건을 지정하는 함수이고, 두번째 인수는 대상 리스트이다.

def flunk(s):
    return s<60

score = [45,89,72,53,94]
for s in filter(flunk, score):
    print(s)
# 45와 53만 출력


# 2) map
# map 함수는 모든 요소에 대해 변환 함수를 호출하여 새 요소값으로 구성된 리스트를 생성한다.
# 인수 구조는 filter 함수와 동일하다.

def half(s):
    return s/2

for s in map(half, score):
    print(s, end=',')


# 3) 람다 함수

for s in filter(lambda x:x <60, score):
    print(s)

for s in filter(lambda x:x/2, score):
    print(s)



# ----------------------------------------------------------------------------------------------------

# 3. 컬렉션의 사본

# 1) 리스트의 사본
# 기존에 변수 a,b,가 있고 b= a라 했을 때 a 값이 변경된다고 b 값이 변경되진 않았다. 그러나 컬렉션은 다르다.
# 그 이유는 리스트가 독립된 사본이 아니라 같은 메모리를 가리키는 것으로 되기 때문이다.

list1 = [1,2,3]
list2 = list1

list2[1] = 100
print(list1)
print(list2)
# list1과 list2 둘다 모두 [1,100,3]으로 값이 변경 되어 있다.

# 따라서 독립된 사본을 복사해 다르것을 가리키게 해야하는데 이때, copy 메소드를 이용한다.

list2 = list1.copy()
list3 = list1[:]
# copy 대신 [:]을 이용할수도 있다. [:]은 새로운 리스트를 만들고 그 리스트에 해당 범위의 값을 넣어주는 것이기 떄문이다.

list3[2] = -1
print(list3)


# 2) is 연산자
# 두 변수가 같은 객체를 가리키고 있는지 조사하기 위해서는 is 구문을 사용한다.

print(list1 is list2)