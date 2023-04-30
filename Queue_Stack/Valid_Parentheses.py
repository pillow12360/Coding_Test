def isValid(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif not stack or stack.pop() != i:
            return False
    return not stack
s = "{(([[]]))[]}"

print(isValid(s))

# 직관적 접근방법과 단순화, 극한화
# 활용할 자료구조의 활용

