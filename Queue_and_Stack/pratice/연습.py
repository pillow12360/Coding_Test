temp = [73,74,85,81,69,72,76,73]

def Temperature(t):
    stack = []
    answer = [0] * len(temp)

    for cur_day, cur_temp in enumerate(t):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            answer[prev_day] = cur_day - prev_day 
        stack.append((cur_day,cur_temp))
    return answer

stack = []

stack.append((1,2))
stack.append((3,4))
stack.append((5,6))
stack.append((7,8))

print(stack[-1][1])

print(Temperature(temp))
