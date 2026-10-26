# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 2
# Date: 26 October 2026
# Description: Remove duplicate values while preserving order
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

def unique_values(alist):
    result = []
    for value in alist:
        if value not in result:
            result.append(value)
    return result

alist = [23, 34, 67, 87, 22, 43, 34, 87, 23, 33, 22, 34]
print("Original:", alist)
print("Unique:", unique_values(alist))
print("Empty list test:", unique_values([]))
print("All-same test:", unique_values([5, 5, 5, 5]))
