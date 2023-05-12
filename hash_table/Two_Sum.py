#정수가 저장된 배열 nums가 주어졌을 때, nums의 원소중 두 숫자를 더해서 target이 될 수 있으면 True 불가능하면 False를 반환하시오 같은원소를 두 번 사용할 수 없다.

#메모리를 사용하여 시간복잡도를 효율적으로 줄일 수 있다.

#딕셔너리 구조로 key값에 저장하고자 하는 값에 넣어야함

#key에 리스트에 자료들을 저장
# 일차적으로 value값은 의미없는 True값 저장

#for 반복문을 통해 딕셔너리자료 중 key값에 요소저장

nums = [4,1,9,5,3,16]
target = 14
memo = {} # 딕셔너리 선언
def Two_Sum(nums,target):
  for v in nums:
      memo[v]=1
      #ket 값으로 v(요소를 지정하고) 딕셔너리의 요소는 1로 지정

  for v in nums:
      neede_number = target - v
      if neede_number in memo:
          if neede_number == memo[v]:
              return False
          else:
            return True
  return False

print(Two_Sum(nums,target))