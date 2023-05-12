# 점수를 리스트를 이용하여 저장한다.
score = [97, 49, 89]
# 97점이 어느 과목의 점수인지 모른다.

score = {
    'math' : 97,
    "eng" : 49,
    'kor' : 87
}
# key 값으로 value 값의 의미를 알수 있다.

print(score['math'])
# 접근 방법

score['math'] = 45

print(score['math'])

score['sci'] = 100
# 새로운 value 추가

print(score['sci'])

# score['music']
# 존재하지 않는 key로 접근 시 에러 발생

#과목의 수가 매우 많아 어떤 과목이 있는지 확인하고 싶을시

print('music' in score)
# False 반환

if 'music' in score:
    print(score['music'])
else:
    score['music'] = 0
    print(score['music'])

# key의 가지고 있는지 확인하는 in이 강력하다 빅오 O(1)이다.
# 데이터를 찾는데에 다른 방식은 빅오 n 이기 때문에 시간 복잡도를 줄일 핵심방법

# 파이썬의 in 연산이 random access 처럼 동작한다.




