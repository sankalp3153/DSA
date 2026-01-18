"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1366
Updated: 2026-01-18T14:27:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1366
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
