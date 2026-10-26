# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 11
# Date: 26 October 2026
# Description: Validate balanced brackets using a list stack
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

def is_balanced(expr: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in expr:
        if ch in '([{': stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]: return False
    return len(stack) == 0

for expression in ["(a[b]{c})", "([)]", "((x)", "", "no brackets", "{[()()]}", "{[(])}", "]"]:
    print(repr(expression), "->", is_balanced(expression))
