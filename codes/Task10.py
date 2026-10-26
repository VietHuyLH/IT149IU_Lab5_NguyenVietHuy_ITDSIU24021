# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 10
# Date: 26 October 2026
# Description: Matrix transpose, addition, and multiplication using nested lists
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

def transpose(m):
    return [list(row) for row in zip(*m)] if m else []

def add(m1, m2):
    if len(m1) != len(m2) or any(len(a) != len(b) for a, b in zip(m1, m2)):
        raise ValueError("Matrices must have equal dimensions.")
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])): row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

def multiply(m1, m2):
    if not m1 or not m2 or len(m1[0]) != len(m2):
        raise ValueError("Columns of first matrix must equal rows of second.")
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)): result[i][j] += m1[i][k] * m2[k][j]
    return result

def print_matrix(m, title):
    print(title)
    for row in m: print(" ".join(f"{v:>6}" for v in row))

A = [[1, 2, 3], [4, 5, 6]]; B = [[7, 8], [9, 10], [11, 12]]
print_matrix(transpose(A), "transpose(A):")
print_matrix(add(A, [[10, 20, 30], [40, 50, 60]]), "A + D:")
print_matrix(multiply(A, B), "A x B:")
