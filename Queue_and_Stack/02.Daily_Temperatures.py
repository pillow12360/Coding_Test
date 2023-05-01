# 매일의 온도를 나타내는 int형 배열 temperatures가 주어진다.
# answer배열의 원소 answer[i]는 i번 째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다. 만약 더 따듯해지는 날이 없다면 answer[i] == 0 이다. answer 배열을 반환하는 함수를 구현

# 제약 조건 <10^5 (빅오 n^2 이상 불가능) => 완전탐색 x

temp = [73,74,85,81,69,72,76,73]

def Temeratures(t):
    stack = []
    answer = [0]*len(t)
    for cur_day, cur_temp in enumerate(t):
        while stack and stack[-1][1] < cur_temp:
            # stack[-1][1]
            # 스텍의 탑(가장 최근에 저장한 값)에 있는 1번째 인덱스의 온도 .
            # 그값이 현재 온도보다 작으면
            prev_day, _ = stack.pop()
            # stack의 데이터를 pop해주는데 prev_day 는 인덱스 값 대입, _는 요소 인 온도값 저장하는데 필요없으니 _로 설정 
            answer[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return answer

print(Temeratures(temp))