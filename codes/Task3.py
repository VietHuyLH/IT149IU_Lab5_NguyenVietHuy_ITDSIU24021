# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 3
# Date: 26 October 2026
# Description: Insertion sort with a user-provided example list
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

def insertion_sort(values):
    result = values.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

alist = [23, 34, 67, 87, 22, 43, 33, 99, 23, 77]
print("Unsorted:", alist)
print("Sorted:", insertion_sort(alist))
