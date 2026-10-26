# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 6
# Date: 26 October 2026
# Description: Generate, deduplicate and sort 8000 user IDs
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

import random
random.seed(2026)
letters = "abcdef"
ids = [random.choice(letters) + str(random.randint(1, 4)) + str(random.randint(1, 4)) for _ in range(8000)]
unique_ids = sorted(set(ids), reverse=True)
print("Generated IDs:", len(ids))
print("Unique IDs:", len(unique_ids))
print("Maximum possible:", 6 * 4 * 4)
print("Sorted unique IDs:", unique_ids)
