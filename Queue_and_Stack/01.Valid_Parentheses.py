def Valid(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '[':
            stack.append('')
        elif not stack or stack.pop() != i:
            return False
    return False
# 직관적 접근방법과 단순화, 극한화
# # 활용할 자료구조의 활용


# for 문 if 
# not (리스트 이름) 리스트가 끝나거나 
# or stack.pop() != i i와 마지막에 저장된 문자와 비교해보고 그 요소 없애줌 LIFO
# stack

