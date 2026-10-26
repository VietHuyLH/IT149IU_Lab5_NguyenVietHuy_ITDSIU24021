# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 8
# Date: 26 October 2026
# Description: COVID-19 daily case descriptive statistics and bar chart
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

import statistics
import matplotlib.pyplot as plt
cases = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]
print("Minimum:", min(cases))
print("Maximum:", max(cases))
print("Range:", max(cases) - min(cases))
print(f"Mean: {statistics.mean(cases):.2f}")
print(f"Median: {statistics.median(cases):.2f}")
print(f"Sample variance: {statistics.variance(cases):.2f}")
print(f"Sample standard deviation: {statistics.stdev(cases):.2f}")
plt.figure(figsize=(10, 4.8)); plt.bar(range(1, 21), cases)
plt.title("Daily New COVID-19 Cases (First 20 Days)"); plt.xlabel("Day"); plt.ylabel("New cases")
plt.xticks(range(1, 21)); plt.tight_layout(); plt.savefig("../outputs/task8_infection_bar_chart.png", dpi=160, bbox_inches="tight"); plt.show()
