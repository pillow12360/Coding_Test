'''
twoSum 문제
리스트 요소 중 두개를 더해서 target 숫자가 나오면 true 아니면 false

input : nums = [4,1,9,7,5,3,16] target : 14
output : True


일단 처음 직관적인 풀이
2중 for 문
'''
#직관적 풀이
a = [4,1,9,7,5,3,16]
b = 14

def twoSum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return True

    return False

print(twoSum(a,b))

#이 코드는 O(n^2)의 시간 복잡도를 가짐

#알고리즘적 풀이
