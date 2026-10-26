# Student Name: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: Fundamentals of Programming (FoP)
# Lab 5 - Task 9
# Date: 26 October 2026
# Description: Simulate rolling two dice for three trial sizes
# AI assistance: ChatGPT was used for guidance and code review; solutions were reviewed by the student.

import numpy as np
import matplotlib.pyplot as plt

def simulate_two_dice(n_rolls, rng, chunk_size=1_000_000):
    counts = np.zeros(13, dtype=np.int64)
    remaining = n_rolls
    while remaining:
        current = min(chunk_size, remaining)
        die1 = rng.integers(1, 7, size=current, dtype=np.int8)
        die2 = rng.integers(1, 7, size=current, dtype=np.int8)
        counts += np.bincount(die1 + die2, minlength=13)
        remaining -= current
    return counts

rng = np.random.default_rng(2026)
results = {}
for n in (360, 36_000, 36_000_000):
    counts = simulate_two_dice(n, rng); results[n] = counts
    print(f"\nRolls: {n:,}"); print("Sum | Count | Percent")
    for s in range(2, 13): print(f"{s:>3} | {counts[s]:>9,} | {counts[s] / n * 100:>8.3f}%")
    print("Counts sum to N:", int(counts[2:13].sum()) == n)
plt.figure(figsize=(8, 4.8)); plt.bar(range(2, 13), results[36_000_000][2:13])
plt.title("Two-Dice Sum Frequencies (36,000,000 Rolls)"); plt.xlabel("Sum"); plt.ylabel("Frequency"); plt.xticks(range(2, 13))
plt.tight_layout(); plt.savefig("../outputs/task9_two_dice_36000000.png", dpi=160, bbox_inches="tight"); plt.show()
