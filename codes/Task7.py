# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 7
# Date: 26 October 2026
# Description: Simulate FIFO queue using list and collections.deque
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

from collections import deque
queue = []
for value in [3, 2, 1]: queue.append(value)
print("List queue:", queue)
while queue: print("dequeue:", queue.pop(0))
queue = deque([3, 2, 1])
while queue: print("deque popleft:", queue.popleft())
print("list.pop(0) shifts remaining elements (O(n)); deque.popleft() is O(1) approximately.")
