

# 1. 사전
# 사전은 키와 값의 쌍을 저장하는 대용량의 자료구조이다.
# 해시 알고리즘을 사용해 일대일로 대응되는 특성이 있어 맵이라고도 부르고 관련된 키와 값의 쌍이라고 해서 연관배열이라고도 한다.


# 1) 키와 값의 쌍
# 사전을 정의할 때는 {} 괄호 안에 키:값 형태로 콤마로 구분하여 나열한다.
# 키 값은 변경이 불가능하다. 따라서 튜플은 키로 사용가능하나 리스트로는 불가능하다.
# 사전은 임의로 내부에서 가장 찾기 빠른 순으로 나열되므로 출력시에 입력순과 다를 수 있다. 
# 사전은 키의 중복을 허용하지 않는다.

dicTmp = dict() # 이러한 방법으로 빈 사전을 정의할 수 있다.


dic = {'boy':'소년', 'school':'학교', 'book':'책'} # 키 : 값
print(dic)
print(dic['boy']) #소년 출력

# get함수는 사전에 없는 키일때 예외 발생이 아닌 None을 출력하도록 하는 함수이다.
print(dic.get('student'))
print(dic.get('student', '사전에 없는 단어 입니다.'))

print(dic.keys())
print(dic.values())
print(dic.items())
