# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 5
# Date: 26 October 2026
# Description: Sort and summarize hardware invoice tuples
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

from operator import itemgetter
invoices = [
    ('83', 'Electric sander', 7, 57.98),
    ('24', 'Power saw', 18, 99.99),
    ('7', 'Sledge hammer', 11, 21.50),
    ('77', 'Hammer', 76, 11.99),
    ('39', 'Jig saw', 3, 79.50),
]
print("a) By description:")
for row in sorted(invoices, key=itemgetter(1)): print(row)
print("\nb) By unit price:")
for row in sorted(invoices, key=itemgetter(3)): print(row)
print("\nc) Description and quantity:")
for row in sorted([(desc, qty) for _, desc, qty, _ in invoices], key=itemgetter(1)): print(row)
values = sorted([(desc, round(qty * price, 2)) for _, desc, qty, price in invoices], key=itemgetter(1))
print("\nd) Invoice values:")
for desc, value in values: print(f"{desc}: ${value:.2f}")
print("\ne) Values from $200 to $500:")
for desc, value in values:
    if 200 <= value <= 500: print(f"{desc}: ${value:.2f}")
total = sum(qty * price for _, _, qty, price in invoices)
print(f"\nf) Total: ${total:.2f}")
