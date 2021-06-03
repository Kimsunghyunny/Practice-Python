

# 1. 함수와 인수

# 파이썬에서 함수는 def로 선언한다.

def test(n):
    sum = 0
    for num in range (n+1):
        sum+= num
    return sum

print("~4=", test(4))


#파이썬에서는 함수를 항상 먼저 정의해놔야 하기때문에 함수를 나중에 구현할 계획이라면 pass를 이용해야한다.



# ----------------------------------------------------------------------------------------------------
# 2. 인수와 형식

#가변변수
#가변인수는 모든 인수를 다 포함하기 때문에 인수 목록의 마지막에 와야한다.

def intsum(s, *ints):
    sum = 0
    for num in ints:
        sum += num
    print (s)
    return sum

print(intsum("ss",1,2,3)) ## ss 와 6을 차례대로 출력


# 인자에 기본값을 지정해줄 수 있다.
def cal(begin, end, step =1):
    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return num

print(cal(1,10,2)) #9
print(cal(1,10)) #10


# 키워드 가변 인수
#키워드 인수를 가변 개수 전달할 때는 인수 목록에 ** 기호를 붙인다.

def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']
    

    sum = 0

    for num in range(begin, end+1, step):
        sum += num

    return sum

print(calcstep(begin=3, end =5, step =1)) #12



# ----------------------------------------------------------------------------------------------------
# 3. 변수의 범위

#지역 변수 - 함수 안에서만 사용되는 변수
# 전역변수 - 함수 밖에서 선언하고 전역에 걸쳐 사용할 수 있는 변수
